from agents import Agent
from tools.web_search import web_search

def create_research_agent():
    agent = Agent(
        name="Research_Agent",
        instructions="You are a research assistant. Your job is to find the most relevant and up-to-date information on the web. " \
        "You will receive queries from the user and you will use the web search tool to find the information. " \
        "Your goal is to provide the user with the best possible answer to their question. ",
        tools=[web_search],
    )

    return agent