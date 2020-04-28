from typing import Mapping
from concepttordf import Contact, Definition
from concepttordf.betydningsbeskrivelse import RelationToSource
from datacatalogtordf import PeriodOfTime


def create_contact(contactpoint: Mapping) -> Contact:
    contact = Contact()

    contact.name = {"nb": contactpoint.get("name", "")}
    contact.email = contactpoint["email"]

    return contact


def create_temporal_coverage(temporal: Mapping) -> PeriodOfTime:
    period = PeriodOfTime()

    period.start_date = temporal["from"]
    period.end_date = temporal["to"]

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


