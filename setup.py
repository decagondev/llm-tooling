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
