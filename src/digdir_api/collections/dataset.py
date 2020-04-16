import os
from concepttordf import Concept, Definition, Contact, AlternativFormulering
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

    def _convert_to_concept(self, hit) -> Concept:
        c = Concept()
        c.identifier = self._concept_identifier + hit["_id"]
        c.term = {"name": {"nb": hit["_source"]["title"]}}
        definition = Definition()
        definition.text = {"nb": hit["_source"]["description"]}

        try:
            definition.remark = {"nb": hit["_source"]["readme"]}
        except KeyError:
            definition.remark = {"nb": ""}

        contact = Contact()

        try:
            contact.email = hit["_source"]["contactpoint"]["email"]
            contact.name = {"nb": hit["_source"]["contactpoint"]["name"]}
        except KeyError:
            contact.email = hit["_source"]["creator"]["email"]
            contact.name = {"nb": hit["_source"]["creator"]["name"]}

        c.contactpoint = contact
        c.definition = definition

        c.validinperiod = {
                           "Gyldig fra og med": hit["_source"]["temporal"]["from"],
                           "Gyldig til og med": hit["_source"]["temporal"]["to"]
                           }

        c.bruksomrade = {"nb": hit["_source"]["theme"][0]}
        c.publisher = os.environ["PUBLISHER"]

        return c
