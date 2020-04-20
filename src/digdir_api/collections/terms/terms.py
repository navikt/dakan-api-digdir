import os
import requests
import datetime as dt
from concepttordf import Concept, Definition, Collection


class TermCollection:

    def __init__(self):
        self._term_collection_id = os.environ["COLLECTION_IDENTIFIER"]
        self._term_collection_name = os.environ["TERM_COLLECTION_NAME"]
        self._term_collection_publisher = os.environ["COLLECTION_PUBLISHER"]
        self._term_concept_id = os.environ["TERM_CONCEPT_IDENTIFIER"]
        self._concept_type = os.environ["TERM_CONCEPT_TYPE"]

    async def create(self):
        collection = Collection()
        collection.identifier = self._term_collection_id
        collection.name = {"nb": self._term_collection_name}
        collection.publisher = self._term_collection_publisher

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

        return collection.to_rdf()

    def _convert_to_concept(self, hit) -> Concept:
        c = Concept()
        c.identifier = self._term_concept_id + hit["_id"]
        c.term = {"name": {"nb": hit["_source"]["title"]}}
        definition = Definition()
        definition.text = {"nb": hit["_source"]["content"]["begrepsforklaring"]}
        c.definition = definition

        c.publisher = os.environ["PUBLISHER"]
        try:
            c.bruksomrade = {"nb": hit["_source"]["content"]["fagomrade"]}
        except KeyError:
            c.bruksomrade = {"nb": ""}

        date = dt.datetime.strptime(hit["_source"]["content"]["oppdatert"].split('T')[0], "%Y-%m-%d")
        c.modified = dt.date(year=date.year, month=date.month, day=date.day)
        return c
