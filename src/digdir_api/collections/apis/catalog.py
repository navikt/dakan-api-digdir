import os

from datacatalogtordf import Catalog
from digdir_api.collections import utils
from digdir_api.collections.apis import api


def create_catalog():
    catalog = Catalog()

    _add_dataservices(catalog)


def _add_dataservices(catalog: Catalog, size: int=10000):
    es_hits = utils.get_es_docs_of_type(doc_type=os.environ["API_CONCEPT_TYPE"], size=size)

    for es_hit in es_hits:
        import pprint
        pprint.pprint(es_hit)
        


