from typing import Mapping
from datacatalogtordf import Distribution


def create_distribution(resource: Mapping) -> Distribution:
    distribution = Distribution()

    _add_mandatory_distribution_props(distribution, resource)
    _add_optional_distribution_props(distribution, resource)

    return distribution


def _add_mandatory_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.formats.append(resource["format"])
    distribution.access_URL = resource["path"]


def _add_optional_distribution_props(distribution: Distribution, resource: Mapping) -> None:
    distribution.title = resource["name"]
    distribution.description = resource["description"]
    distribution.download_URL = resource["path"]
