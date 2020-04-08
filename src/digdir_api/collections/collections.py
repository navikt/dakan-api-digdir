import os
import requests
from abc import ABC, abstractmethod
from typing import Mapping
from concepttordf import Collection


class BaseCollection(ABC):

    def __init__(self, collection_identifier, collection_name, collection_publisher, concept_identifier, concept_type):
        self._collection_identifier = collection_identifier
        self._collection_name = collection_name
        self._collection_publisher = collection_publisher
        self._concept_identifier = concept_identifier
        self._concept_type = concept_type

    async def create(self):
        collection = Collection()
        collection.identifier = self._collection_identifier
        collection.name = {"nb": self._collection_name}
        collection.publisher = self._collection_publisher

        return self._populate_collection(collection)

    def _populate_collection(self, collection: Collection, size: int=10000):
        res = requests.post(os.environ["ES_INDEX_ENDPOINT"],
                            json={
                                "size": size,
                                "query": {
                                    "match": {
                                        "type": self._concept_type
                                    }
                                }
                            })

        for hit in res.json()["hits"]["hits"]:
            concept = self._convert_to_concept(hit)
            collection.members.append(concept)

        return collection.to_rdf().decode()

    @abstractmethod
    def _convert_to_concept(self, hit: Mapping):
        raise NotImplementedError()
