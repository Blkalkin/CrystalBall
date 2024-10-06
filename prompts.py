from agent import Agent

def get_process_agents_system_prompt():
    return f"""You are to role-play as various individuals or institutions making investment decisions based on provided contexts. Your responses should be formatted as a simple JSON-like string that can be converted using .jsonify. Include the following keys in your response:
"direction": either "BUY", "SELL", or "HOLD"
"strength": a float from 0.0 to 1.0 describing the strength of the decision
"rationale": a brief rationale behind your decision and its likelihood/probability"""


def get_process_agents_user_prompt(agent: Agent, event_context: str):
    return f"""You are playing the role of {agent.name}, who or which is a {agent.type}. Here's a description of your investment approach and you: {agent.description}

A recent event has come up in the news and social media: {event_context}

Tell me how you would react in this particular scenario. Particularly, would you buy, sell, or hold based on this event? If you are taking a direction (buy or sell), how likely are you to make that decision given the context on a scale of 0.0 (would not buy or sell/doesn't affect your decision) to 1.0 (definitely buying or selling).
"""


def get_final_reasoning_system_prompt():
    return f"""You are a sophisticated financial analysis AI designed to aggregate and interpret investment decisions from a diverse group of 1,000 personas, including individuals and institutions. Your primary focus is on analyzing reactions to specific events and their potential impact on the S&P 500 index.
Your tasks are as follows:

Aggregate the decisions (BUY, SELL, HOLD) from all 1,000 personas, calculating the percentage for each decision.
Calculate a weighted average probability for BUY and SELL decisions, using the provided probability scores.
Determine the overall market sentiment based on the aggregated data:

"BULLISH" if the weighted BUY probability is significantly higher than SELL.
"BEARISH" if the weighted SELL probability is significantly higher than BUY.
"NEUTRAL" if the probabilities are close or if HOLD is the dominant decision.


Identify and summarize the most common themes and rationales behind the collective sentiment.
Highlight any notable divergences in opinion among different types of investors (e.g., institutional vs. retail).

Your response must be a JSON-like string containing the following keys:

"market_prediction": "BULLISH", "BEARISH", or "NEUTRAL"
"buy_percentage": Float (0.0 to 100.0)
"sell_percentage": Float (0.0 to 100.0)
"hold_percentage": Float (0.0 to 100.0)
"weighted_buy_probability": Float (0.0 to 1.0)
"weighted_sell_probability": Float (0.0 to 1.0)
"summary": String (concise analysis of the overall sentiment and key factors)
"notable_divergences": String (any significant differences in opinion among investor types)"""


def get_final_reasoning_agent_prompt(agent_dict: str, event_context: str):
    return f"""Analyze the market sentiment for the S&P 500 index in response to the following event:
{event_context}
You have been provided with responses from about 1,000 diverse personas, each representing different types of investors. Each response is in a JSON-like format with the following structure:
{{
  "name": "Investor/Institution Name",
  "category": "Investor Type (e.g., Mutual Fund, Retail Investor)",
  "direction": "BUY" or "SELL" or "HOLD",
  "probability": Float (0.0 to 1.0, 0.0 for HOLD),
  "rationale": "Brief explanation for the decision"
}}
Based on these responses, perform your analysis as outlined in the system prompt. Ensure your response is a properly formatted JSON-like string that can be parsed using .jsonify().

Here are the responses from the 1,000 personas:
{agent_dict}
"""


def get_toolhouse_helper_question_type_prompt(event_context: str):
    return f"""
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


def get_toolhouse_real_context_prompt(agent_name: str, question_type: str):
    return f"""
    Use web_search and perplexity_byok to find me information on {agent_name} general investing strategy, how have they reacted to past {question_type} \
        and how has it impacted their investment strategies and concrete decisions (if any)
    """

