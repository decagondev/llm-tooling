from llm_tool_project.tools.tool_loader import ToolLoader

def main():
    tool_loader = ToolLoader()
    tool_loader.load_tool('openai')
    response = tool_loader.call_tool('openai', prompt="Hello, world!")
    print(response)

if __name__ == "__main__":
    main()
