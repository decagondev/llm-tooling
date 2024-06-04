import unittest
from llm_tooling.tools.tool_loader import ToolLoader

class TestToolLoader(unittest.TestCase):
    def setUp(self):
        self.tool_loader = ToolLoader()

    def test_load_tool(self):
        self.tool_loader.load_tool('openai')
        self.assertIn('openai', self.tool_loader.tools)

    def test_call_tool(self):
        self.tool_loader.load_tool('openai')
        response = self.tool_loader.call_tool('openai', prompt="Hello, world!")
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
