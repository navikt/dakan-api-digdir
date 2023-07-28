import os
import datetime as dt
from typing import Mapping
from concepttordf import Concept
from dakan_api_digdir.collections import utils


def create_concept(es_hit: Mapping) -> Concept:
    term = Concept()
    _add_mandatory_concept_props(term, es_hit)
    _add_optional_concept_props(term, es_hit)

    return term


def _add_mandatory_concept_props(concept, es_hit) -> None:
    content = es_hit["content"]
    concept.identifier = es_hit["id"]
    concept.alternativeterm = {"name": {"nb": [utils.remove_new_line(content.get("synonym"))]}}
    concept.hiddenterm = {"name": {"nb": [utils.remove_new_line(content.get("fraraadd_term"))]}}
    concept.term = {
        "name": {
            "nb": utils.remove_new_line(es_hit["title"]),
            "nn": utils.remove_new_line(content.get("termNN")),
            "en": utils.remove_new_line(content.get("termEN"))
        }
    }
    text = {
        "nb": utils.remove_new_line(content.get("clean_definisjon")),
        "nn": utils.remove_new_line(content.get("clean_definisjonNN")),
        "en": utils.remove_new_line(content.get("clean_definisjonEN"))
    }
    source = {
        "text": {
            "nb": utils.remove_new_line(content.get("clean_kilde"))
        }
    }
    concept.definition = utils.create_definition(text, source, content.get("forhold_til_kilde"))
    concept.publisher = os.environ["PUBLISHER"]


def _add_optional_concept_props(concept, es_hit) -> None:
    try:
        concept.subject = {
            "nb": utils.remove_new_line(es_hit["content"]["clean_komponenter"]),
            "nn": "",
            "en": ""
        }
    except KeyError:
        concept.subject = {
            "nb": "",
            "nn": "",
            "en": ""
        }

    concept.contactpoint = utils.create_contact({"contactPoint": {"email": os.environ["TERM_CONCEPT_CONTACT"]}})

    date = dt.datetime.strptime(es_hit["content"]["oppdatert"].split('T')[0], "%Y-%m-%d")
    concept.modified = dt.date(year=date.year, month=date.month, day=date.day)
