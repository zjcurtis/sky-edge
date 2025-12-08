from datetime import datetime
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel
from requests import Response

from ..util import FuzzyDate, HttpMethods, api_request


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


class ConstituentSearchResult(BaseModel):
    id: str
    address: str | None = None
    deceased: bool = False
    email: str | None = None
    fundraiser_status: str | None = None
    inactive: bool = False
    lookup_id: str | None = None
    name: str | None = None
    number_of_subsidiaries: int | None = None

    def to_constituent(self) -> Constituent:
        return Constituent(id=self.id, name=self.name)


class Relationship(BaseModel):
    id: str | None = None
    comment: str | None = None
    constituent_id: str
    date_added: datetime | None = None
    date_modified: datetime | None = None
    end: FuzzyDate | None = None
    is_organization_contact: bool | None = None
    is_primary_business: bool | None = None
    is_spouse: bool | None = None
    is_spouse_head_of_household: bool | None = None
    is_constituent_head_of_household: bool | None = None
    name: str | None = None
    organization_contact_type: str | None = None
    position: str | None = None
    reciprocal_relationship_id: str | None = None
    reciprocal_type: str | None = None
    relation_id: str | None = None
    start: FuzzyDate | None = None
    type: str | None = None
    first_name: str | None = None
    last_name: str | None = None


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


class Note(BaseModel):
    id: str | None = None
    constituent_id: str | None = None
    date: FuzzyDate | None = None
    summary: str | None = None
    text: str | None = None
    type: str | None = None
    author: str | None = None


T = TypeVar("T")


class Collection(BaseModel, Generic[T]):
    count: int
    next_link: Optional[str] = None
    value: List[T]

    def fetch_next(self) -> Optional["Collection[T]"] | Response:
        if not self.next_link:
            return None
        else:
            return api_request(
                method=HttpMethods.GET, url=self.next_link, response_model=Collection[T]
            )


class CollectionOfAddresses(Collection[Address]):
    pass


class CollectionOfConstituentSearchResults(Collection[ConstituentSearchResult]):
    pass


class CollectionOfRelationships(Collection[Relationship]):
    pass


class CollectionOfEmails(Collection[Email]):
    pass


class CollectionOfPhones(Collection[Phone]):
    pass


class CollectionOfAliases(Collection[Alias]):
    pass


class CollectionOfStrings(Collection[str]):
    pass


class CollectionOfNotes(Collection[Note]):
    pass


def address_post(address: Address) -> Address | Response:
    response = api_request(
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
            return response


def address_delete(address: Address) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/addresses/{address.id}",
    )


def address_list_constituent_get(
    constituent_id: str, include_inactive: bool = False
) -> CollectionOfAddresses | Response:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/addresses"
    if include_inactive:
        url = f"{url}?include_inactive=true"

    return api_request(
        method=HttpMethods.GET, url=url, response_model=CollectionOfAddresses
    )


def constituent_get(constituent_id: str) -> Constituent | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}",
        response_model=Constituent,
    )


def constituent_search_get(
    search_text: str,
    fundraiser_status: list[str] | None = None,
    include_inactive: bool = False,
    search_field: str | None = None,
    strict_search: bool = False,
    include_non_constituents: bool = False,
    limit: int = 500,
    offset: int | None = None
) -> CollectionOfConstituentSearchResults | Response:
    params = {
        "search_text": search_text,
        "fundraiser_status": fundraiser_status,
        "include_inactive": include_inactive,
        "search_field": search_field,
        "strict_search": strict_search,
        "include_non_constituents": include_non_constituents,
        "limit": limit,
        "offset": offset
    }
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/constituents/search",
        response_model=CollectionOfConstituentSearchResults,
        params=params,
    )


def constituent_patch(constituent: Constituent) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent.id}",
        data=constituent.model_dump_json(exclude_none=True),
    )


def email_list_all_get(**kwargs) -> CollectionOfEmails | Response:
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/emailaddresses",
        response_model=CollectionOfEmails,
        **kwargs,
    )


def email_list_constituent_get(constituent_id: str) -> CollectionOfEmails | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/emailaddresses",
        response_model=CollectionOfEmails,
    )


def email_delete(email: Email) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email.id}",
    )


def phone_list_constituent_get(constituent_id: str) -> CollectionOfPhones | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/phones",
        response_model=CollectionOfPhones,
    )


def phone_delete(phone: Phone) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/phones/{phone.id}",
    )


def alias_list_constituent_get(
    constituent_id: str, include_inactive: bool = False
) -> CollectionOfAliases | Response:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/aliases"
    if include_inactive:
        url = f"{url}?include_inactive=true"

    return api_request(
        method=HttpMethods.GET, url=url, response_model=CollectionOfAliases
    )


def alias_collection_post(
    aliases: CollectionOfAliases,
) -> CollectionOfStrings | Response:
    return api_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/aliases",
        response_model=CollectionOfStrings,
        data=aliases.model_dump_json(exclude_none=True),
    )


def alias_patch(alias: Alias) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/aliases/{alias.id}",
        data=alias.model_dump_json(exclude_none=True, exclude={"id", "constituent_id"}),
    )


def alias_delete(alias: Alias) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/aliases/{alias.id}",
    )


def relationship_list_constituent_get(
    constituent_id: str,
) -> CollectionOfRelationships | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/relationships",
        response_model=CollectionOfRelationships,
    )


def relationship_patch(relationship: Relationship) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/relationships/{relationship.id}",
        data=relationship.model_dump_json(
            exclude_none=True, exclude={"id", "constituent_id"}
        ),
    )


def relationship_delete(relationship: Relationship) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/relationships/{relationship.id}",
    )


def note_post(note: Note) -> Note | Response:
    response = api_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/addresses",
        data=note.model_dump_json(exclude_none=True),
    )
    match response.status_code:
        case 200:
            if response.json()["id"]:
                note.id = response.json()["id"]
            return note
        case _:
            return response


def note_list_constituent_get(
    constituent_id: str,
) -> CollectionOfNotes | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/notes",
        response_model=CollectionOfNotes,
    )
