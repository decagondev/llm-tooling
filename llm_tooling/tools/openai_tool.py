import openai
import yaml
from llm_tool_project.utils.logger import Logger

class OpenaiTool:
    def __init__(self):
        self.logger = Logger()
        with open('llm_tooling/config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            self.api_key = config['openai']['api_key']
        openai.api_key = self.api_key

    def call(self, prompt):
        self.logger.log(f"Calling OpenAI with prompt: {prompt}")
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=100
        )
        self.logger.log(f"Received response: {response}")
        return response.choices[0].text.strip()
