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
    concept.term = {"name": {"nb": es_hit["title"]}}
    concept.definition = utils.create_definition({"nb": es_hit["content"]["begrepsforklaring"]})


def _add_optional_concept_props(concept, es_hit) -> None:
    concept.publisher = os.environ["PUBLISHER"]

    try:
        concept.bruksomrade = {"nb": es_hit["content"]["fagomrade"]}
    except KeyError:
        concept.bruksomrade = {"nb": ""}

    date = dt.datetime.strptime(es_hit["content"]["oppdatert"].split('T')[0], "%Y-%m-%d")
    concept.modified = dt.date(year=date.year, month=date.month, day=date.day)


