from typing import List
from abc import ABC, abstractmethod
from IPromptBuilder import IPromptBuilder

class PromptBuilder(IPromptBuilder):
    @abstractmethod
    def buildPrompts(self, tableschema: List[str], userPrompt: str) -> List[str]:
        pass

    @abstractmethod
    def ShowPrompts(self) -> None:
        pass
