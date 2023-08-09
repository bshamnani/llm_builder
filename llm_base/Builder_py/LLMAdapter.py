from LLMClient import LLMClient
from GPTClient import GPTClient

class LLMAdapter:
    @staticmethod
    def get_llm_instance() -> LLMClient:
        llm_client = GPTClient()
        return llm_client
