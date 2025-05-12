#this is a test interface for the agents
import asyncio
from agents import Runner, RunConfig
from providers.ollama_provider import CustomModelProvider
from Agents.orchestrator_agent import create_orchestrator_agent

CUSTOM_MODEL_PROVIDER = CustomModelProvider()

def print_agent_info(agent):
    print(f"Agent Name: {agent.name}")
    print(f"Instructions: {agent.instructions}")
    print(f"Tools: {[tool.name for tool in agent.tools]}")
    print()

def print_intro():
    print("\n" + "-" * 50)
    print("Welcome to Test Interface".center(50))
    print("-" * 50)
    print("This is a test interface for the agents.")

async def main(): 
    testAgent = create_orchestrator_agent()
    print_agent_info(testAgent)
    print_intro()
    
    while True:
        try: 
            user_input = input("Enter your query (or 'exit'): ")
            if user_input.lower() == 'exit':
                break

            print("\nProcessing your query...")
            response = await Runner.run(
                testAgent,
                user_input,
                run_config=RunConfig(
                    model_provider = CUSTOM_MODEL_PROVIDER,
                )
            )
            print(f"AI: {response.final_output}")
        
        except KeyboardInterrupt:
            print("\nExiting")
            break
        except Exception as e:
            import traceback
            print(f"An error occurred: {e}")
            traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())


