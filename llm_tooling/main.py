from llm_tool_project.tools.tool_loader import ToolLoader
from llm_tool_project.prompts.prompt_loader import PromptLoader

def main():
    tool_loader = ToolLoader()
    tool_loader.load_tool('openai')

    prompt_loader = PromptLoader()
    prompt_content = prompt_loader.load_prompt('example_prompt.txt')

    response = tool_loader.call_tool('openai', prompt=prompt_content)
    print(response)

if __name__ == "__main__":
    main()
