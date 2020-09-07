import os
from isodate import parse_date
from typing import Mapping

import requests
from concepttordf import Contact, Definition
from concepttordf.betydningsbeskrivelse import RelationToSource
from datacatalogtordf import PeriodOfTime


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
