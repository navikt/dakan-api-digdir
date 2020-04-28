from typing import Mapping
from datacatalogtordf import Distribution, URI
from digdir_api.collections import utils


def create_distribution(resource: Mapping) -> Distribution:
    distribution = Distribution()

    _add_mandatory_distribution_props(distribution, resource)
    _add_optional_distribution_props(distribution, resource)

    return distribution


def _add_mandatory_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.formats.append(resource["format"])
    distribution.access_URL = URI(resource["path"])
    distribution.identifier = URI(resource["path"])


def _add_optional_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.title = {"nb": resource["name"]}
    distribution.description = {"nb": utils.remove_new_line(resource["description"])}
    distribution.download_URL = URI(resource["path"])
