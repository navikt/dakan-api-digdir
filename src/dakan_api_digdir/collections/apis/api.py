import os

from datacatalogtordf import DataService, URI
from typing import Mapping


def create_api(es_hit: Mapping) -> DataService:
    api = DataService()
    _add_mandatory_props(api, es_hit)
    _add_optional_props(api, es_hit)

    return api


def _add_mandatory_props(api: DataService, es_hit: Mapping) -> None:
    api.title = {"nb": es_hit["title"]}
    api.identifier = f"{os.environ['API_CONCEPT_IDENTIFIER']}/{es_hit['id']}"
    api.publisher = URI(os.environ["PUBLISHER"])
    if es_hit.get("master") == "NAV API PORTAL":
        api.landing_page = [os.environ["NAV_API_PORTAL"]]


def _add_optional_props(api: DataService, es_hit: Mapping) -> None:
    api.description = {"nb": es_hit["content"].get("clean_description", es_hit["content"]["description"])}
    try:
        api.endpointURL = es_hit["content"]["url"]
    except KeyError:
        pass

    if es_hit["content"].get("swagger", es_hit["content"].get("api_dec")):
        api.endpointDescription = es_hit["content"].get("swagger", es_hit["content"].get("api_dec"))
