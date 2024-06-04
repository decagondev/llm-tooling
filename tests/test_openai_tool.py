import unittest
from llm_tooling.tools.openai_tool import OpenaiTool

class TestOpenaiTool(unittest.TestCase):
    def setUp(self):
        self.openai_tool = OpenaiTool()

    def test_call(self):
        response = self.openai_tool.call(prompt="Hello, world!")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
