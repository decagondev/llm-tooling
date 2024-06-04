import importlib
from llm_tool_project.tools.base_tool import BaseTool

class ToolLoader:
    def __init__(self):
        self.tools = {}

    def load_tool(self, tool_name):
        module = importlib.import_module(f'llm_tool_project.tools.{tool_name}_tool')
        tool_class = getattr(module, f'{tool_name.capitalize()}Tool')
        if issubclass(tool_class, BaseTool):
            self.tools[tool_name] = tool_class()
        else:
            raise TypeError(f"{tool_name.capitalize()}Tool must inherit from BaseTool")

    def call_tool(self, tool_name, **kwargs):
        if tool_name in self.tools:
            return self.tools[tool_name].call(**kwargs)
        else:
            raise ValueError(f"Tool {tool_name} not loaded.")
