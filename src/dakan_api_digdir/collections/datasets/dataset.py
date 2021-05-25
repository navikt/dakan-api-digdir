import os
import requests
from typing import Mapping
from datacatalogtordf import Dataset, URI
from dakan_api_digdir.collections.datasets import distribution
from dakan_api_digdir.collections import utils
from dakan_api_digdir.collections.datasets.distribution import create_html_distribution


def create_dataset(es_hit: Mapping) -> Dataset:
    dataset = Dataset()
    _add_mandatory_dataset_props(dataset, es_hit)
    _add_optional_dataset_props(dataset, es_hit)
    _add_distributions(dataset, es_hit["id"])

    return dataset


def _add_mandatory_dataset_props(dataset: Dataset, es_hit: Mapping) -> None:
    dataset.title = {"nb": utils.remove_new_line(es_hit["title"])}
    dataset.identifier = URI(os.environ["DATASET_CONCEPT_IDENTIFIER"] + es_hit["id"])
    dataset.landing_page = [os.environ["DATASET_CONCEPT_IDENTIFIER"] + es_hit["id"]]
    dataset.description = {"nb": es_hit["description"]}
    dataset.publisher = URI(os.environ["PUBLISHER"])
    dataset.language = utils.create_language(es_hit["language"])
    dataset.access_rights = utils.create_access_rights(es_hit["accessRights"])
    dataset.spatial_coverage = utils.create_location(es_hit["spatial"])


def _add_optional_dataset_props(dataset: Dataset, es_hit: Mapping) -> None:
    dataset.contactpoint = utils.create_contact(es_hit)
    dataset.creator = URI(os.environ["PUBLISHER"])
    dataset.frequency = URI(es_hit.get("periodicity", ""))
    dataset.license = URI(es_hit["license"]["url"])
    dataset.temporal_coverage = utils.create_temporal_coverage(es_hit["temporal"])


def _add_distributions(dataset: Dataset, package_id: str):
    dp_metadata = requests.get(f"{os.environ['BUCKET_ENDPOINT']}/{package_id}/datapackage.json").json()

    html_distribution = create_html_distribution(dp_metadata)
    dataset.distributions.append(html_distribution)

    for resource in dp_metadata["resources"]:
        dist = distribution.create_distribution(resource)
        dataset.distributions.append(dist)
