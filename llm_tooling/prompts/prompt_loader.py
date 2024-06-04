import os

class PromptLoader:
    def __init__(self, prompt_dir='llm_tooling/prompts'):
        self.prompt_dir = prompt_dir

    def list_prompts(self):
        return [f for f in os.listdir(self.prompt_dir) if os.path.isfile(os.path.join(self.prompt_dir, f))]

    def load_prompt(self, prompt_name):
        prompt_path = os.path.join(self.prompt_dir, prompt_name)
        if not os.path.exists(prompt_path):
            raise FileNotFoundError(f"Prompt {prompt_name} not found in {self.prompt_dir}")
        with open(prompt_path, 'r') as file:
            return file.read()

    def save_prompt(self, prompt_name, content):
        prompt_path = os.path.join(self.prompt_dir, prompt_name)
        with open(prompt_path, 'w') as file:
            file.write(content)
