from MetadataManager import MetadataManager
from KQLMetadataManager import KQLMetadataManager

class DomainAdapter:
    @staticmethod
    def getMetadataManager() -> MetadataManager:
        metadataManager = KQLMetadataManager()
        return metadataManager
