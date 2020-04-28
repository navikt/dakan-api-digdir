import os
import datetime as dt
from typing import Mapping
from concepttordf import Concept
from digdir_api.collections import utils


def create_concept(es_hit: Mapping) -> Concept:
    term = Concept()
    _add_mandatory_concept_props(term, es_hit)
    _add_optional_concept_props(term, es_hit)

    return term


def _add_mandatory_concept_props(concept, es_hit) -> None:
    concept.identifier = os.environ["TERM_CONCEPT_IDENTIFIER"] + es_hit["id"]
    concept.term = {
        "name": {"nb": utils.remove_new_line(es_hit["title"])}
    }
    concept.definition = utils.create_definition({"nb": utils.remove_new_line(es_hit["content"]["begrepsforklaring"])},
                                                 {"text": {"nb": utils.remove_new_line(es_hit["content"]["kilde"])}})
    concept.publisher = os.environ["PUBLISHER"]


def _add_optional_concept_props(concept, es_hit) -> None:
    try:
        concept.subject = {"nb": [utils.remove_new_line(es_hit["content"]["fagomrade"])]}
    except KeyError:
        concept.subject = {"nb": ""}

    concept.contactpoint = utils.create_contact({"email": os.environ["TERM_CONCEPT_CONTACT"]})

    date = dt.datetime.strptime(es_hit["content"]["oppdatert"].split('T')[0], "%Y-%m-%d")
    concept.modified = dt.date(year=date.year, month=date.month, day=date.day)
