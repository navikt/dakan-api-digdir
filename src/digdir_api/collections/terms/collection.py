import os

from concepttordf import Collection
from digdir_api.collections.terms import concept
from digdir_api.collections import utils


def create_collection() -> str:
    collection = Collection()
    _add_mandatory_collection_props(collection)
    _add_concepts(collection)

    return collection.to_rdf().decode()


def _add_mandatory_collection_props(collection) -> None:
    collection.identifier = os.environ["COLLECTION_IDENTIFIER"]
    collection.description = {"nb": "NAV godkjente begreper"}
    collection.name = {"nb": os.environ["TERM_COLLECTION_NAME"]}
    collection.publisher = os.environ["PUBLISHER"]


def _add_concepts(collection: Collection, size=10000) -> None:
    es_hits = utils.get_es_docs_of_type(doc_type=os.environ["TERM_CONCEPT_TYPE"], size=size)

    for es_hit in es_hits:
        term = concept.create_concept(es_hit["_source"])
        collection.members.append(term)
