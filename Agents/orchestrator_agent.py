from agents import Agent
from Agents.research_agent import create_research_agent
from Agents.context_agent import create_context_agent

def create_orchestrator_agent():
    agent = Agent(
        name="Orchestrator_Agent",
        instructions="You are an orchestrator of a multi-agent system. " \
        "Your job is to take user input and pass it to the appropriate tool agent. You will receive tasks from the user "
        "and delegate them to the appropriate agents based on their expertise. Ensure that the tasks are completed efficiently and " \
        "effectively. You may need to use multiple agents to get all of the information you need. Do not mention the agents or tools you are using. " \
        "Your goal is to provide the user with the best possible answer to their question. ",  
        tools=[create_research_agent().as_tool(
            tool_name="Research_Agent",
            tool_description="Searches the web for information and provides the most relevant and up-to-date information."),
            create_context_agent().as_tool(
            tool_name="Context_Agent",
            tool_description="Extracts structured, relevant information from a user's description of their business and returns a clean, concise business context profile.")
            ]
    )

    return agent