import csv
from typing import List, Dict


def create_agents_from_csv(csv_file_path: str) -> List[Dict]:
    agents = []
    
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            agent = {
                'type': row['Type'],
                'name': row['Name'],
                'description': row['Description'],
                'isReal': False,
                'output': ''
            }
            agents.append(agent)
    
    return agents



# Example usage:
agents = create_agents_from_csv('/Users/balaji/Downloads/AgentTestData.csv') # use your own data file

print(agents)