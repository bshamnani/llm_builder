from NLPProvider import INLPProvider
from UserNLPClient import UserNLPClient

class NLPAdapter:
    @staticmethod
    def getNLPClient(persona: str) -> UserNLPClient:
        nlpClient = UserNLPClient()
        return nlpClient
