from abc import ABC, abstractmethod


class BaseLLMProvider(ABC):
    @abstractmethod
    def summarize(self, text: str) -> str:
        pass
