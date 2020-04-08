import os
from concepttordf import Concept, Definition
from digdir_api.collections.collections import BaseCollection


class DatasetCollection(BaseCollection):

    def __init__(self):
        super().__init__(
            collection_identifier=os.environ["COLLECTION_IDENTIFIER"],
            collection_name=os.environ["DATASET_COLLECTION_NAME"],
            collection_publisher=os.environ["COLLECTION_PUBLISHER"],
            concept_identifier=os.environ["DATASET_CONCEPT_IDENTIFIER"],
            concept_type=os.environ["DATASET_CONCEPT_TYPE"]
        )

    def _convert_to_concept(self, hit):
        c = Concept()
        c.identifier = self._concept_identifier + hit["_id"]
        c.term = {"name": {"nb": hit["_source"]["title"]}}
        definition = Definition()
        definition.text = {"nb": hit["_source"]["description"]}
        c.definition = definition
        return c
