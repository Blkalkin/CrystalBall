import asyncio
import csv
import json
from typing import Dict, List

from groq import AsyncGroq

from model import Agent, Direction, LLMResponse
from prompts import get_process_agents_system_prompt, get_process_agents_user_prompt


def create_agents_from_csv(csv_file_path: str) -> List[Agent]:
    agents = []
    
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            agent = Agent(
                type=row['Type'],
                name=row['Name'],
                description=row['Description'],
                isReal=False
            )
            agents.append(agent)
    
    return agents


async def process_agents_with_groq(agents: List[Agent]) -> List[Agent]:
    client = AsyncGroq()
    
    async def process_agent(agent: Agent):
        system_prompt = get_process_agents_system_prompt()
        
        user_prompt = get_process_agents_user_prompt(agent)
        
        try:
            chat_completion = await client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                model="llama3-8b-8192",
            )
            
            response_content = chat_completion.choices[0].message.content
            print(f"Raw LLM response: {response_content}")  # Add this line for debugging
            
            llm_response = json.loads(response_content)
            
            agent.llmResponse = LLMResponse(
                direction=Direction(llm_response["direction"]),
                strength=float(llm_response["strength"]),
                rationale=llm_response["rationale"]
            )
        except json.JSONDecodeError as e:
            print(f"JSON parsing error for agent {agent.name}: {str(e)}")
            agent.llmResponse = LLMResponse(
                direction=Direction.HOLD,
                strength=0.0,
                rationale="Error in processing response"
            )
        except Exception as e:
            print(f"Error processing agent {agent.name}: {str(e)}")
            agent.llmResponse = LLMResponse(
                direction=Direction.HOLD,
                strength=0.0,
                rationale="Error in processing response"
            )
        
        return agent

    tasks = [process_agent(agent) for agent in agents]
    processed_agents = await asyncio.gather(*tasks)
    
    return processed_agents

async def process_agents(csv_file_path: str) -> List[Agent]:
    agents = create_agents_from_csv(csv_file_path)
    return await process_agents_with_groq(agents)

async def run_agent_processing(csv_file_path: str) -> List[Dict]:
    processed_agents = await process_agents(csv_file_path)
    return [agent.dict() for agent in processed_agents]


# Example usage:
# agents = create_agents_from_csv('/Users/balaji/Downloads/AgentTestData.csv') # use your own data file
