import openai
import asyncio
from typing import List
from LLMClient import LLMClient


openai.api_type = "azure"
openai.api_base = "https://syntheticsoai.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "d12cf2ed7e14418ab2fb6783b3414e1a"



class GPTClient(LLMClient): 
    def __init__(self):
        super().__init__()
        self.model_name = "syntheticsKQL"


    async def get_completions_async(self, prompts: List[str]) -> str:
        final_prompt = "\n"
        for prompt in prompts:
            final_prompt +="\n" + prompt + "\n"

        #final_prompt = "\n".join(prompts)
        print(final_prompt)

        completionsResponse = openai.Completion.create(
            engine="syntheticsKQL",
            #engine="Test-bhavesh",
            prompt = final_prompt,
            #temperature=0,
            #nucleus_sampling_factor=9,
            #max_tokens=500,
            #frequency_penalty=0,
            #presence_penalty=0,
            top_p=1,
            best_of=1,
            stop=["#",";"],
            temperature=LLMClient().temperature,
            max_tokens=LLMClient().max_tokens,
            frequency_penalty = LLMClient().frequency_penalty,
            presence_penalty = LLMClient().presence_penalty,
        )

        completions = completionsResponse.values
        responseKQL = completionsResponse.choices[0]["text"]
        print(responseKQL)
        return responseKQL

    def invoke_llm_command_async(self, prompts: List[str], model: str) -> str:
        kql_query = self.get_completions_async(prompts)
        return kql_query










