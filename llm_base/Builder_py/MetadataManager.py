from typing import List
from abc import ABC, abstractmethod

from IMetadataManager import IMetadataManager

class MetadataManager(IMetadataManager):
    @abstractmethod
    def getObjectMetadata(self, objectName: List[str]) -> List[str]:
        pass
