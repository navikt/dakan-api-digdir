from typing import Mapping
from concepttordf import Contact
from datacatalogtordf import PeriodOfTime, InvalidDateError


def create_contact(contactpoint: Mapping):
    contact = Contact()
    try:
        contact.name = contactpoint["name"]
        contact.email = contactpoint["email"]
    except KeyError:
        contact.name = ""
        contact.email = ""

    return contact


def create_temporal_coverage(temporal: Mapping):
    period = PeriodOfTime()
    try:
        period.start_date = temporal["from"]
        period.end_date = temporal["to"]
    except InvalidDateError:
        print("huff")

    return period
