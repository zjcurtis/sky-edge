from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from ..auth import AppTokens
from ..util import HttpMethods, generic_request


class Phone(BaseModel):
    id: str
    constituent_id: str
    date_added: datetime
    date_modified: datetime
    do_not_call: bool
    inactive: bool
    number: str
    primary: bool
    type: str


class Email(BaseModel):
    id: str
    address: str
    constituent_id: str
    date_added: datetime
    date_modified: datetime
    do_not_email: bool
    inactive: bool
    primary: bool
    type: str


class CollectionOfEmails(BaseModel):
    count: int
    value: List[Email]
    next_link: Optional[str] = None


class CollectionOfPhones(BaseModel):
    count: int
    value: List[Phone]
    next_link: Optional[str] = None


def email_list_all_get(apptokens: AppTokens, **kwargs) -> CollectionOfEmails | int:
    response = generic_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/emailaddresses",
        apptokens=apptokens,
        **kwargs,
    )
    match response.status_code:
        case 200:
            return CollectionOfEmails(**response.json())
        case _:
            return response.status_code


def email_list_constituent_get(
    constituent_id: str, apptokens: AppTokens
) -> CollectionOfEmails | int:
    response = generic_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/emailaddresses",
        apptokens=apptokens,
    )
    match response.status_code:
        case 200:
            return CollectionOfEmails.model_validate_json(json_data=response.text)
        case _:
            return response.status_code


def email_delete(email: Email, apptokens: AppTokens) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email.id}",
        apptokens=apptokens,
    ).status_code


def phone_list_constituent_get(
    constituent_id: str, apptokens: AppTokens
) -> CollectionOfPhones | int:
    response = generic_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/phones",
        apptokens=apptokens,
    )
    match response.status_code:
        case 200:
            return CollectionOfPhones(**response.json())
        case _:
            return response.status_code


def phone_delete(phone: Phone, apptokens: AppTokens) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/phones/{phone.id}",
        apptokens=apptokens,
    ).status_code
