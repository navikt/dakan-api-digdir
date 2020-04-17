import os
import requests

from typing import Mapping
from concepttordf import Contact
from datacatalogtordf import Catalog, Dataset, Distribution, PeriodOfTime, URI, InvalidDateError


class DatapackageCatalog:

    async def create(self) -> str:
        catalog = Catalog()
        catalog.title = {"nb": "NAV åpne datapakker"}
        catalog.identifier = os.environ["COLLECTION_IDENTIFIER"]

        return self._populate_catalog(catalog)

    def _populate_catalog(self, catalog: Catalog, size=10000) -> str:
        res = requests.post(os.environ["ES_INDEX_ENDPOINT"],
                            json={
                                "size": size,
                                "query": {
                                    "match": {
                                        "type": "datapackage"
                                    }
                                }
                            })

        for hit in res.json()["hits"]["hits"]:
            dataset = self._convert_to_dataset(hit["_source"])
            catalog.datasets.append(dataset)

        return catalog.to_rdf()

    def _convert_to_dataset(self, hit: Mapping) -> Dataset:
        dataset = Dataset()

        dataset.title = {"nb": hit["title"]}
        dataset.identifier = os.environ["DATASET_CONCEPT_IDENTIFIER"] + hit["id"]
        dataset.description = hit["description"]
        dataset.publisher = os.environ["PUBLISHER"]

        dataset.contactpoint = self._create_contact(hit)
        dataset.creator = os.environ["PUBLISHER"]
        dataset.access_rights = hit["accessRights"]
        dataset.frequency = hit.get("periodicity", "")

        dataset.license = self._create_license(hit)
        dataset.temporal_coverage = self._create_temporal_coverage(hit)
        dataset.language = hit["language"]

        return self._add_distributions(dataset, hit["url"])

    def _add_distributions(self, dataset: Dataset, metadata_url: str) -> Dataset:
        res = requests.get(metadata_url)

        for resource in res.json()["resources"]:
            distribution = self._create_distribution(resource)
            dataset.distributions.append(distribution)

        return dataset

    @staticmethod
    def _create_distribution(resource: Mapping) -> Distribution:
        distribution = Distribution()

        distribution.description = resource["description"]
        distribution.title = resource["name"]
        distribution.access_URL = resource["path"]
        distribution.download_URL = resource["path"]

        return distribution

    @staticmethod
    def _create_contact(hit):
        contact = Contact()
        try:
            contact.name = hit["contactpoint"]["name"]
            contact.email = hit["contactpoint"]["email"]
        except KeyError:
            contact.name = ""
            contact.email = ""

        return contact

    @staticmethod
    def _create_license(hit):
        return URI(hit["license"]["url"])

    @staticmethod
    def _create_temporal_coverage(hit):
        period = PeriodOfTime()
        try:
            period.start_date = hit["temporal"]["from"]
            period.end_date = hit["temporal"]["to"]
        except InvalidDateError:
            print(hit["title"])

        return period
