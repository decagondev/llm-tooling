import unittest
import os
from llm_tool_project.prompts.prompt_loader import PromptLoader

class TestPromptLoader(unittest.TestCase):
    def setUp(self):
        self.prompt_loader = PromptLoader()
        self.test_prompt_name = 'test_prompt.txt'
        self.test_prompt_content = 'This is a test prompt.'

    def tearDown(self):
        try:
            os.remove(os.path.join(self.prompt_loader.prompt_dir, self.test_prompt_name))
        except FileNotFoundError:
            pass

    def test_save_prompt(self):
        self.prompt_loader.save_prompt(self.test_prompt_name, self.test_prompt_content)
        saved_content = self.prompt_loader.load_prompt(self.test_prompt_name)
        self.assertEqual(saved_content, self.test_prompt_content)

    def test_load_prompt(self):
        with open(os.path.join(self.prompt_loader.prompt_dir, self.test_prompt_name), 'w') as file:
            file.write(self.test_prompt_content)
        loaded_content = self.prompt_loader.load_prompt(self.test_prompt_name)
        self.assertEqual(loaded_content, self.test_prompt_content)

    def test_list_prompts(self):
        prompt_list = self.prompt_loader.list_prompts()
        self.assertIn('example_prompt.txt', prompt_list)

if __name__ == '__main__':
    unittest.main()
