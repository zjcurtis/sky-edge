from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from ..auth import AppTokens
from ..util import HttpMethods, generic_request


@dataclass
class ConstituentId:
    value: str


@dataclass
class PhoneId:
    value: str


@dataclass
class EmailId:
    value: str


@dataclass
class Phone:
    id: PhoneId
    constituent_id: ConstituentId
    date_added: datetime
    date_modified: datetime
    do_not_call: bool
    inactive: bool
    number: str
    primary: bool
    type: str


@dataclass
class Email:
    id: EmailId
    address: str
    constituent_id: ConstituentId
    date_added: datetime
    date_modified: datetime
    do_not_email: bool
    inactive: bool
    primary: bool
    type: str


@dataclass
class CollectionOfEmails:
    count: int
    value: List[Email]
    next_link: Optional[str] = None


@dataclass
class CollectionOfPhones:
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
    constituent_id: ConstituentId, apptokens: AppTokens
) -> CollectionOfEmails | int:
    response = generic_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id.value}/emailaddresses",
        apptokens=apptokens,
    )
    match response.status_code:
        case 200:
            return CollectionOfEmails(**response.json())
        case _:
            return response.status_code


def email_delete(email_id: EmailId, apptokens: AppTokens) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email_id.value}",
        apptokens=apptokens,
    ).status_code


def phone_list_constituent_get(
    constituent_id: ConstituentId, apptokens: AppTokens
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


def phone_delete(phone_id: PhoneId, apptokens: AppTokens) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/phones/{phone_id.value}",
        apptokens=apptokens,
    ).status_code
