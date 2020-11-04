import os

from typing import Mapping
from datacatalogtordf import Distribution, URI
from digdir_api.collections import utils
from digdir_api.collections.utils import create_format


def create_html_distribution(dp_metadata: dict):
    html_distribution = Distribution()
    html_distribution.title = {"nb": dp_metadata["title"]}
    html_distribution.formats = ["text/html"]
    html_distribution.description = {"nb": dp_metadata["description"]}
    html_distribution.identifier = URI(os.environ["DATASET_CONCEPT_IDENTIFIER"] + dp_metadata["id"])
    html_distribution.license = URI("http://creativecommons.org/licenses/by/4.0/deed.no")
    html_distribution.access_URL = URI(os.environ["DATASET_CONCEPT_IDENTIFIER"] + dp_metadata["id"])
    return html_distribution


def create_distribution(resource: Mapping) -> Distribution:
    distribution = Distribution()

    _add_mandatory_distribution_props(distribution, resource)
    _add_optional_distribution_props(distribution, resource)

    return distribution


def _add_mandatory_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.formats = [create_format(resource["format"])]
    distribution.access_URL = URI(resource["path"])
    distribution.identifier = URI(resource["path"])
    distribution.license = URI("http://creativecommons.org/licenses/by/4.0/deed.no")


def _add_optional_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.title = {"nb": resource["name"].replace("_", " ").capitalize()}
    distribution.description = {"nb": utils.remove_new_line(resource["description"])}
    distribution.download_URL = URI(resource["path"])
