import os
import datetime as dt

from concepttordf import Concept, Definition
from digdir_api.collections.collections import BaseCollection


class TermCollection(BaseCollection):

    def __init__(self):
        super().__init__(
            collection_identifier=os.environ["COLLECTION_IDENTIFIER"],
            collection_name=os.environ["TERM_COLLECTION_NAME"],
            collection_publisher=os.environ["COLLECTION_PUBLISHER"],
            concept_identifier=os.environ["TERM_CONCEPT_IDENTIFIER"],
            concept_type=os.environ["TERM_CONCEPT_TYPE"]
        )

    def _convert_to_concept(self, hit) -> Concept:
        c = Concept()
        c.identifier = self._concept_identifier + hit["_id"]
        c.term = {"name": {"nb": hit["_source"]["title"]}}
        definition = Definition()
        definition.text = {"nb": hit["_source"]["content"]["begrepsforklaring"]}
        c.definition = definition

        c.publisher = os.environ["PUBLISHER"]
        # try:
        #     c.bruksomrade = {"nb": hit["_source"]["content"]["fagomrade"]}
        # except KeyError:
        #     c.bruksomrade = {"nb": ""}

        date = dt.datetime.strptime(hit["_source"]["content"]["oppdatert"].split('T')[0], "%Y-%m-%d")
        c.modified = dt.date(year=date.year, month=date.month, day=date.day)
        return c
