from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel

from ..util import FuzzyDate, HttpMethods, generic_request


class Address(BaseModel):
    id: str | None = None
    address_lines: str | None = None
    city: str | None = None
    constituent_id: str
    country: str | None = None
    county: str | None = None
    date_added: datetime | None = None
    date_modified: datetime | None = None
    do_not_mail: bool | None = None
    end: datetime | None = None
    formatted_address: str | None = None
    inactive: bool | None = None
    postal_code: str | None = None
    preferred: bool | None = None
    seasonal_end: FuzzyDate | None = None
    seasonal_start: FuzzyDate | None = None
    start: datetime | None = None
    state: str | None = None
    suburb: str | None = None
    type: str
    region: str | None = None
    information_source: str | None = None
    lot: str | None = None
    cart: str | None = None
    dpc: str | None = None


class Constituent(BaseModel):
    id: str | None = None
    address: Address | None = None
    age: int | None = None
    birthdate: FuzzyDate | None = None
    date_added: datetime | None = None
    date_modified: datetime | None = None
    deceased: bool | None = None
    deceased_date: FuzzyDate | None = None
    first: str | None = None
    former_name: str | None = None
    gender: str | None = None
    gives_anonymously: bool | None = None
    inactive: bool | None = None
    last: str | None = None
    lookup_id: str | None = None
    marital_status: str | None = None
    middle: str | None = None
    name: str | None = None
    preferred_name: str | None = None
    suffix: str | None = None
    suffix_2: str | None = None
    title: str | None = None
    title_2: str | None = None
    birthplace: str | None = None
    ethnicity: str | None = None
    income: str | None = None
    religion: str | None = None
    industry: str | None = None
    matches_gifts: bool | None = None
    matching_gift_per_gift_min: str | None = None
    matching_gift_per_gift_max: str | None = None
    matching_gift_total_min: str | None = None
    matching_gift_total_max: str | None = None
    matching_gift_factor: float | None = None
    matching_gift_notes: str | None = None
    num_employees: int | None = None
    is_memorial: bool | None = None
    is_solicitor: bool | None = None
    no_valid_address: bool | None = None
    receipt_type: str | None = None
    target: str | None = None
    requests_no_email: bool | None = None
    num_subsidiaries: int | None = None
    parent_corporation_id: int | None = None
    parent_corporation_name: str | None = None


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


class Alias(BaseModel):
    id: str | None = None
    constituent_id: str
    name: str | None = None
    type: str | None = None


class Collection(BaseModel):
    count: int
    next_link: Optional[str] = None


class CollectionOfAddresses(Collection):
    value: List[Address]


class CollectionOfEmails(Collection):
    value: List[Email]


class CollectionOfPhones(Collection):
    value: List[Phone]


class CollectionOfAliases(Collection):
    value: List[Alias]


class CollectionOfStrings(Collection):
    value: List[str]


def address_post(address: Address) -> Address | int:
    response = generic_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/addresses",
        data=address.model_dump_json(exclude_none=True),
    )
    match response.status_code:
        case 200:
            if response.json()["id"]:
                address.id = response.json()["id"]
            return address
        case _:
            return response.status_code


def address_delete(address: Address) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/addresses/{address.id}",
    ).status_code


def address_list_constituent_get(
    constituent_id: str, include_inactive: bool = False
) -> CollectionOfAddresses | int:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/addresses"
    if include_inactive:
        url = f"{url}?include_inactive=true"

    response = generic_request(
        method=HttpMethods.GET,
        url=url,
    )
    match response.status_code:
        case 200:
            return CollectionOfAddresses.model_validate_json(json_data=response.text)
        case _:
            return response.status_code

def constituent_get(
    constituent_id: str
) -> Constituent | int:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}"

    response = generic_request(
        method=HttpMethods.GET,
        url=url,
    )
    match response.status_code:
        case 200:
            return Constituent.model_validate_json(json_data=response.text)
        case _:
            return response

def constituent_patch(constituent: Constituent):
    return generic_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent.id}",
        data=constituent.model_dump_json(exclude_none=True),
    ).status_code
    

def email_list_all_get(**kwargs) -> CollectionOfEmails | int:
    response = generic_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/emailaddresses",
        **kwargs,
    )
    match response.status_code:
        case 200:
            return CollectionOfEmails(**response.json())
        case _:
            return response.status_code


def email_list_constituent_get(constituent_id: str) -> CollectionOfEmails | int:
    response = generic_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/emailaddresses",
    )
    match response.status_code:
        case 200:
            return CollectionOfEmails.model_validate_json(json_data=response.text)
        case _:
            return response.status_code


def email_delete(email: Email) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email.id}",
    ).status_code


def phone_list_constituent_get(constituent_id: str) -> CollectionOfPhones | int:
    response = generic_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/phones",
    )
    match response.status_code:
        case 200:
            return CollectionOfPhones(**response.json())
        case _:
            return response.status_code


def phone_delete(phone: Phone) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/phones/{phone.id}",
    ).status_code


def alias_list_constituent_get(
    constituent_id: str, include_inactive: bool = False
) -> CollectionOfAliases | int:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/aliases"
    if include_inactive:
        url = f"{url}?include_inactive=true"

    response = generic_request(
        method=HttpMethods.GET,
        url=url,
    )
    match response.status_code:
        case 200:
            return CollectionOfAliases.model_validate_json(json_data=response.text)
        case _:
            return response.status_code


def alias_collection_post(aliases: CollectionOfAliases) -> CollectionOfStrings | int:
    response = generic_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/aliases",
        data=aliases.model_dump_json(exclude_none=True),
    )
    match response.status_code:
        case 200:
            return CollectionOfStrings.model_validate_json(json_data=response.text)
        case _:
            return response.status_code


def alias_patch(alias: Alias) -> int:
    return generic_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/aliases/{alias.id}",
        data=alias.model_dump_json(exclude_none=True, exclude={"id", "constituent_id"}),
    ).status_code


def alias_delete(alias: Alias) -> int:
    return generic_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/aliases/{alias.id}",
    ).status_code
