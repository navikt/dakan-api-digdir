import os

from datacatalogtordf import Catalog, URI
from digdir_api.collections.datasets import dataset
from digdir_api.collections import utils


def create_catalog() -> str:
    catalog = Catalog()
    _add_mandatory_catalog_props(catalog)
    _add_optional_catalog_props(catalog)
    _add_datasets(catalog)

    return catalog.to_rdf().decode()


def _add_mandatory_catalog_props(catalog: Catalog) -> None:
    catalog.title = {"nb": "NAV åpne datapakker"}
    catalog.identifier = os.environ["COLLECTION_IDENTIFIER"]
    catalog.publisher = URI(os.environ["PUBLISHER"])


def _add_optional_catalog_props(catalog: Catalog) -> None:
    catalog.homepage = URI(os.environ["CATALOG_HOMEPAGE"])


def _add_datasets(catalog: Catalog, size=10000) -> None:
    es_hits = utils.get_es_docs_of_type(doc_type=os.environ["DATASET_CONCEPT_TYPE"], size=size)

    for es_hit in es_hits:
        ds = dataset.create_dataset(es_hit["_source"])
        catalog.datasets.append(ds)
