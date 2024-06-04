import importlib

class ToolLoader:
    def __init__(self):
        self.tools = {}

    def load_tool(self, tool_name):
        module = importlib.import_module(f'llm_tooling.tools.{tool_name}_tool')
        tool_class = getattr(module, f'{tool_name.capitalize()}Tool')
        self.tools[tool_name] = tool_class()

    def call_tool(self, tool_name, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name].call(**kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not loaded.")
