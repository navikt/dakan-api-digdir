import os

from datacatalogtordf import Catalog, URI
from digdir_api.collections import utils
from digdir_api.collections.apis import api


def create_catalog():
    catalog = Catalog()

    _add_dataservices(catalog)
    _add_mandatory_catalog_props(catalog)
    _add_optional_catalog_props(catalog)

    print(catalog.to_rdf().decode())

    return catalog.to_rdf().decode()


def _add_dataservices(catalog: Catalog, size: int = 10000):
    es_hits = utils.get_es_docs_of_type(doc_type=os.environ["API_CONCEPT_TYPE"], size=size)
    for es_hit in es_hits:
        data_service = api.create_api(es_hit["_source"])
        catalog.services.append(data_service)
        break


def _add_mandatory_catalog_props(catalog: Catalog) -> None:
    catalog.title = {"nb": "NAV åpne APIer"}
    catalog.identifier = os.environ["COLLECTION_IDENTIFIER"]
    catalog.publisher = URI(os.environ["PUBLISHER"])


def _add_optional_catalog_props(catalog: Catalog) -> None:
    catalog.homepage = URI(os.environ["CATALOG_HOMEPAGE"])
