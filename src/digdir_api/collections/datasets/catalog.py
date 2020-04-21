import os
import requests
from datacatalogtordf import Catalog, URI
from digdir_api.collections.datasets import dataset


def create_catalog() -> str:
    catalog = Catalog()
    _add_mandatory_catalog_props(catalog)
    _add_optional_catalog_props(catalog)
    _add_datasets(catalog)

    return catalog.to_rdf()


def _add_mandatory_catalog_props(catalog: Catalog) -> None:
    catalog.title = {"nb": "NAV åpne datapakker"}
    catalog.identifier = os.environ["COLLECTION_IDENTIFIER"]
    catalog.publisher = URI(os.environ["PUBLISHER"])


def _add_optional_catalog_props(catalog: Catalog) -> None:
    catalog.homepage = URI(os.environ["CATALOG_HOMEPAGE"])


def _add_datasets(catalog: Catalog, size=10000) -> None:
    res = requests.post(os.environ["ES_INDEX_ENDPOINT"],
                        json={
                            "size": size,
                            "query": {
                                "match": {
                                    "type": "datapackage"
                                }
                            }
                        })

    for es_hit in res.json()["hits"]["hits"]:
        ds = dataset.create_dataset(es_hit["_source"])
        catalog.datasets.append(ds)
