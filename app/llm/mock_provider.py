from app.llm.base import BaseLLMProvider


class MockLLMProvider(BaseLLMProvider):
    def summarize(self, text: str) -> str:
        return f"Summary: {text[:200]}"
