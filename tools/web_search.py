from duckduckgo_search import DDGS
from agents import function_tool

@function_tool
def web_search(query: str) -> str:
    """
    Perform a web search using DuckDuckGo and return the first result.
    """
    with DDGS() as ddgs:
        results = ddgs.text(query)
        if results and len(results) > 0:
            return results[0]['body']
        else:
            return "No results found."
        

def main():
    # Example usage
    query = "What is Linsanity?"
    with DDGS() as ddgs:
        results = ddgs.text(query)
    print(results)

if __name__ == "__main__":
    main()