import os
import requests
from typing import Mapping
from datacatalogtordf import Dataset, URI
from digdir_api.collections.datasets import distribution
from digdir_api.collections import utils


def create_dataset(es_hit: Mapping) -> Dataset:
    dataset = Dataset()
    _add_mandatory_dataset_props(dataset, es_hit)
    _add_optional_dataset_props(dataset, es_hit)
    _add_distributions(dataset, es_hit["url"])

    return dataset


def _add_mandatory_dataset_props(dataset: Dataset, es_hit: Mapping) -> None:
    dataset.title = {"nb": utils.remove_new_line(es_hit["title"])}
    dataset.identifier = URI(os.environ["DATASET_CONCEPT_IDENTIFIER"] + es_hit["id"])
    dataset.description = {"nb": es_hit["description"]}
    dataset.publisher = URI(os.environ["PUBLISHER"])


def _add_optional_dataset_props(dataset: Dataset, es_hit: Mapping) -> None:
    dataset.contactpoint = utils.create_contact(es_hit)
    dataset.creator = URI(os.environ["PUBLISHER"])
    dataset.access_rights = URI(es_hit["accessRights"])
    dataset.frequency = URI(es_hit.get("periodicity", ""))

    dataset.license = URI(es_hit["license"]["url"])
    dataset.temporal_coverage = utils.create_temporal_coverage(es_hit["temporal"])
    dataset.language = [es_hit["language"]]


def _add_distributions(dataset: Dataset, metadata_url: str):
    res = requests.get(metadata_url)

    for resource in res.json()["resources"]:
        dist = distribution.create_distribution(resource)
        dataset.distributions.append(dist)
