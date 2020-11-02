import os
from isodate import parse_date
from typing import Mapping, Any

import requests
from concepttordf import Contact, Definition
from concepttordf.betydningsbeskrivelse import RelationToSource
from datacatalogtordf import PeriodOfTime, Location, URI


def create_contact(es_hit: Mapping) -> Contact:
    contact = Contact()

    try:
        contact.name = {"nb": es_hit["contactPoint"].get("name", "")}
        contact.email = es_hit["contactPoint"]["email"]
    except (KeyError, AttributeError):
        contact.name = {"nb": es_hit["creator"].get("name", "")}
        contact.email = es_hit["creator"]["email"]

    return contact


def create_temporal_coverage(temporal: Mapping) -> PeriodOfTime:
    period = PeriodOfTime()

    period.start_date = parse_date(temporal["from"]).strftime("%Y-%m-%d")
    period.end_date = parse_date(temporal["to"]).strftime("%Y-%m-%d")

    return period


def create_location(spatial: str) -> Location:
    location = Location()
    if spatial.lower() in ["norge", "norway"]:
        print("riktig location")
        location.identifier = URI("http://sws.geonames.org/3144096/")
    return location


def create_format(dist_format):
    return "text/csv" if dist_format.lower() == "csv" else dist_format


def get_language_uri(language):
    if language.lower() in ["norsk", "norwegian", "nor"]:
        return "http://publications.europa.eu/resource/authority/language/NOR"
    elif language.lower() in ["engelsk", "english", "en"]:
        return "http://publications.europa.eu/resource/authority/language/ENG"
    else:
        return language


def create_language(language: Any):
    return [get_language_uri(language)] if isinstance(language, str) else [get_language_uri(l) for l in language]


def create_access_rights(acces_rights: str):
    return "http://publications.europa.eu/resource/authority/access-right/PUBLIC" \
        if acces_rights.lower() in ["open", "opendata", "åpne data"] else acces_rights


def create_definition(text: Mapping, source: Mapping) -> Definition:
    definition = Definition()
    definition.text = text
    definition.relationtosource = RelationToSource.basertPaKilde
    definition.source = source
    return definition


def remove_new_line(string: str) -> str:
    try:
        new_string = string.replace("\n", "").replace("\r", "")
    except AttributeError:
        new_string = ''
    return new_string


def get_es_docs_of_type(doc_type: str, size: int):
    res = requests.post(os.environ["ES_INDEX_ENDPOINT"],
                        json={
                            "size": size,
                            "query": {
                                "match": {
                                    "type": doc_type
                                }
                            }
                        })

    return res.json()["hits"]["hits"]


def remove_prefix(dist: bytes):
    dist_str = dist.decode()
    dist_lines = dist_str.splitlines()
    dist_str = '\n'.join(dist_lines[2:])

    return dist_str.encode()
