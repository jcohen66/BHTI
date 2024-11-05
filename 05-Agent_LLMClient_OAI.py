# Define the Agent base structure
class Agent:
    """
    Integrates LLM client, tools, and memory.
    """
    def __init__(self, llm_client=None, tools=None, memory=None):
        self.llm_client = llm_client
        self.tools = tools
        self.memory = memory

    def run(self):
        """
        Placeholder for the agent's main execution logic.
        """
        pass
    
from typing import Dict, Any, List
import openai

# Define the LLM Client
class OpenAIChatCompletion:
    """
    Interacts with OpenAI's API for chat completions.
    """
    def __init__(self, model: str, api_key: str = None, base_url: str = None):
        """
        Initialize with model, API key, and base URL.
        """
        self.client = openai.OpenAI(api_key=api_key, base_url=base_url)
        self.model = model

    def generate(self, messages: List[Dict], **kwargs) -> Dict[str, Any]:
        """
        Generate a response from input messages.
        """
        params = {'messages': messages, 'model': self.model, **kwargs}
        response = self.client.chat.completions.create(**params)
        return response.choices[0].message
    
# Integrate the LLM client with the AI Agent
class Agent:
    """
    Integrates LLM client, tools, and memory.
    """
    def __init__(self, llm_client, tools=None, memory=None):
        self.llm_client = llm_client
        self.tools = tools
        self.memory = memory

    def run(self, messages: List[Dict[str, str]]):
        """
        Generates a response from the LLM client.
        """
        # Generate response using the LLM client
        response = self.llm_client.generate(messages)
        return response
    
# Test the client
# API from environment variable
# import os
# api_key = os.getenv("OPENAI_API_KEY"))
import os
api_key=os.environ.get("OPENAI_API_KEY")

client = OpenAIChatCompletion(
    base_url='https://api.openai.com/v1',
    model='gpt-4',
    api_key=api_key
)

# Define a set of messages
messages = [
    {"role": "system", "content": "You are a security assistant."},
    {"role": "user", "content": "Hey! This is Roberto!"}
]

# Initialize the agent with the LLM client
myAgent = Agent(llm_client=client)

# Use the agent to run a task
response = myAgent.run(messages=messages)
print(response)
print("\n\nFinal Answer: \n\n")
print(response.to_dict())