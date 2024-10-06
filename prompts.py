def get_process_agents_system_prompt():
    return """You are role playing this person in a market scenario where the rates are going down 1 point, and your response should be a json where the keys are: "direction" which is either "BUY", "SELL" or "HOLD"
"strength" which is a float from 0.0 to 1.0, defaulting to 0.0 if direction is "HOLD"
"rationale" which is a brief rationale behind the decision and likeliness/probability"""


def get_process_agents_user_prompt(agent):
    return f"Type: {agent.type}\nName: {agent.name}\nDescription: {agent.description}"


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
