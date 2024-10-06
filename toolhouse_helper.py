import asyncio
import os
from typing import List

import aiohttp
import requests
from dotenv import load_dotenv
from groq import Groq

# 👋 Make sure you've also installed the Groq SDK through: pip install groq
from toolhouse import Toolhouse

from constants import API_URL

load_dotenv()

MODEL = "llama3-groq-70b-8192-tool-use-preview"


async def get_question_type(event_context: str):
    prompt = f"""
    This is a fictional/ real event context: {event_context}.
    
    Can you tell me what type of question/what domain this question belongs to? I want an answer such that I can input it in a sentence like this: 
    "Find me information on New York Pension Funds general investing strategy, how have they reacted to past _______, and how has it \
        impacted their investment strategies and concrete decisions (if any).

    A few examples are as follows:

    Event Context: "The Federal Reserve has announced a 50 basis points rate hike."
    Question Type: "Federal Rate Hikes"

    Event Context: "The US has announced a new round of tariffs on Chinese goods."
    Question Type: "tariffs on China and other countries"

    Event Context: "North Korea has declared war on South Korea."
    Question Type: "Wars and geopolitical conflicts"

    Event Context: "Taylor Swift has announced a new tour in the UK."
    Question Type: "concerts and other entertainment events by notable artists and celebrities"

    Just give me the question type as a string. Do not return anything else.
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                API_URL + "/chatWithGroq", json={"message": prompt}
            ) as response:
                response_json = await response.json()
                return response_json["response"]
    except Exception as e:
        print(f"Error getting question type: {str(e)}")
        return None


def get_real_context(agent_object, question):
    name = agent_object["name"]

    question_type = get_question_type(question)
    if question_type is None:
        return None

    prompt = f"""
        Use web_search and perplexity_byok to find me information on {name} general investing strategy, how have they reacted to past {question_type} \
            and how has it impacted their investment strategies and concrete decisions (if any)
        """

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    MODEL = "llama3-groq-70b-8192-tool-use-preview"

    # If you don't specify an API key, Toolhouse will expect you
    # specify one in the TOOLHOUSE_API_KEY env variable.
    th = Toolhouse()
    messages = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        # Passes Code Execution as a tool
        tools=th.get_tools("bitsandbills"),
    )

    # Runs the Code Execution tool, gets the result,
    # and appends it to the context
    tool_run = th.run_tools(response)
    messages.extend(tool_run)

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=th.get_tools("bitsandbills"),
    )

    return response.choices[0].message.content
