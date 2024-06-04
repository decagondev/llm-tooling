from abc import ABC, abstractmethod

class BaseTool(ABC):
    @abstractmethod
    def call(self, **kwargs):
        pass
