from tools.tool_loader import ToolLoader
from prompts.prompt_loader import PromptLoader

def main():
    tool_loader = ToolLoader()
    tool_loader.load_tool('openai')
    tool_loader.load_tool('weather')

    prompt_loader = PromptLoader()
    prompt_content = prompt_loader.load_prompt('example_prompt.txt')

    openai_response = tool_loader.call_tool('openai', prompt=prompt_content)
    print("OpenAI Response:", openai_response)

    weather_response = tool_loader.call_tool('weather', city='London')
    print("Weather Response:", weather_response)

if __name__ == "__main__":
    main()
