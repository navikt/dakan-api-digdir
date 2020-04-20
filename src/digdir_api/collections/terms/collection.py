import os
import requests


from concepttordf import Collection
from digdir_api.collections.terms import concept


def create_collection() -> str:
    collection = Collection()
    _add_mandatory_collection_props(collection)
    _add_concepts(collection)

    return collection.to_rdf()


def _add_mandatory_collection_props(collection) -> None:
    collection.identifier = os.environ["COLLECTION_IDENTIFIER"]
    collection.description = {"nb": "NAV godkjente begreper"}
    collection.name = {"nb": os.environ["TERM_COLLECTION_NAME"]}
    collection.publisher = os.environ["PUBLISHER"]


def _add_concepts(collection: Collection, size=10000) -> None:
    res = requests.post(os.environ["ES_INDEX_ENDPOINT"],
                        json={
                            "size": size,
                            "query": {
                                "match": {
                                    "type": os.environ["TERM_CONCEPT_TYPE"]
                                }
                            }
                        })

    for es_hit in res.json()["hits"]["hits"]:
        term = concept.create_concept(es_hit["_source"])
        collection.members.append(term)
