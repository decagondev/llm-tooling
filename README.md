LLM Tool Project

LLM Tool Project
================

Overview
--------

The LLM Tool Project is designed to facilitate the loading and usage of various Language Model (LM) tools, including those provided by OpenAI. This project structures the tools into a modular library, making it easy to extend and integrate additional tools.

Project Structure
-----------------
```
llm_tooling/
├── README.md
├── setup.py
├── requirements.txt
├── llm_tooling/
│   ├── __init__.py
│   ├── main.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── config.yaml
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── tool_loader.py
│   │   ├── openai_tool.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
├── tests/
│   ├── __init__.py
│   ├── test_tool_loader.py
│   ├── test_openai_tool.py
```
### Description of Key Files and Directories

*   `README.md`: This file. Provides an overview and setup instructions for the project.
*   `setup.py`: Script for setting up the Python package.
*   `requirements.txt`: Lists the dependencies required for the project.
*   `llm_tooling/`: Main project directory containing the codebase.
    *   `__init__.py`: Initializes the Python package.
    *   `main.py`: The main script to run the project.
    *   `config/`: Directory for configuration files.
        *   `config.yaml`: Configuration file in YAML format.
    *   `tools/`: Directory for tool-related modules.
        *   `tool_loader.py`: Module for loading and managing tools.
        *   `openai_tool.py`: Module for wrapping OpenAI API functionality.
    *   `utils/`: Directory for utility modules.
        *   `logger.py`: Module for logging.
*   `tests/`: Directory for unit tests.
    *   `test_tool_loader.py`: Unit tests for the tool loader.
    *   `test_openai_tool.py`: Unit tests for the OpenAI tool.

Setup Instructions
------------------

### Prerequisites

Ensure you have Python 3.6 or higher installed. You can download Python from [python.org](https://www.python.org/).

### Installation

1.  Clone the repository:
    
        git clone https://github.com/yourusername/llm_tooling.git
        cd llm_tooling
    
2.  Create and activate a virtual environment (optional but recommended):
    
        python -m venv venv
        source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    
3.  Install the dependencies:
    
        pip install -r requirements.txt
    
4.  Configure the project by updating `llm_tooling/config/config.yaml` with your OpenAI API key:
    
        openai:
          api_key: "your_openai_api_key"
    

### Running the Project

To run the project, execute the `main.py` script:

    python llm_tooling/main.py

### Running Tests

To run the tests, use the following command:

    pytest

Usage
-----

### Loading and Calling Tools

The `ToolLoader` class is responsible for loading and calling tools. Here is an example of how to use it:

    from llm_tooling.tools.tool_loader import ToolLoader
    
    tool_loader = ToolLoader()
    tool_loader.load_tool('openai')
    response = tool_loader.call_tool('openai', prompt="Hello, world!")
    print(response)

### Adding New Tools

To add a new tool, follow these steps:

1.  Create a new module in the `llm_tooling/tools/` directory, e.g., `new_tool.py`.
2.  Define a class for the tool, e.g., `NewTool`, and implement the necessary methods.
3.  Update the `ToolLoader` class to support the new tool.

Contributing
------------

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code follows the project's coding standards and includes tests where applicable.

License
-------

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

Acknowledgments
---------------

*   [OpenAI](https://www.openai.com/) for providing the API.
*   [PyYAML](https://pyyaml.org/) for YAML parsing.

Code Files
----------

### setup.py

    from setuptools import setup, find_packages
    
    setup(
        name='llm_tooling',
        version='0.1.0',
        packages=find_packages(),
        install_requires=[
            'openai',
            'PyYAML',
            'pytest'
        ],
    )

### requirements.txt

    openai
    PyYAML
    pytest

### main.py

    from llm_tooling.tools.tool_loader import ToolLoader
    
    def main():
        tool_loader = ToolLoader()
        tool_loader.load_tool('openai')
        response = tool_loader.call_tool('openai', prompt="Hello, world!")
        print(response)
    
    if __name__ == "__main__":
        main()

### config/config.yaml

    openai:
      api_key: "your_openai_api_key"

### tools/tool_loader.py

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

### tools/openai_tool.py

    import openai
    import yaml
    from llm_tooling.utils.logger import Logger
    
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

### utils/logger.py

    import logging
    
    class Logger:
        def __init__(self):
            logging.basicConfig(level=logging.INFO)
            self.logger = logging.getLogger(__name__)
    
        def log(self, message):
            self.logger.info(message)

### tests/test_tool_loader.py

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

### tests/test_openai_tool.py

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