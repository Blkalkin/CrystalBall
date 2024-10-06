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
from prompts import (
    get_toolhouse_helper_question_type_prompt,
    get_toolhouse_helper_real_context_prompt,
)

load_dotenv()

MODEL = "llama3-groq-70b-8192-tool-use-preview"


async def get_question_type(event_context: str):
    prompt = get_toolhouse_helper_question_type_prompt(event_context)
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


async def get_real_context(agent_object, question):
    name = agent_object["name"]

    question_type = await get_question_type(question)
    if question_type is None:
        return None

    prompt = get_toolhouse_helper_real_context_prompt(name, question_type)

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

    agent_object["realContext"] = response.choices[0].message.content

    return agent_object
