from datetime import datetime
from enum import StrEnum
from typing import Annotated, Union

from pydantic import BaseModel, Field
from requests import Response

from ..util import Collection, ContentType, FuzzyDate, HttpMethods, api_request


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


class AttachmentType(StrEnum):
    LINK = "Link"
    PHYSICAL = "Physical"


class Attachment(BaseModel):
    date: datetime = datetime.now()
    file_id: str | None = None
    file_name: str | None = None
    name: str | None = None
    parent_id: str
    tags: list[str] | None = None
    thumbnail_id: str | None = None
    type: AttachmentType
    url: str | None = None


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


class ConstituentSearchQuery(BaseModel):
    search_text: str
    fundraiser_status: list[str] | None = None
    include_inactive: bool | None = None
    search_field: str | None = None
    strict_search: bool | None = None
    include_non_constituents: bool | None = None
    limit: Union[Annotated[int, Field(ge=1, le=5000)], None] = None
    offset: int | None = None


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


class ConstituentListQuery(BaseModel):
    constituent_code: list[str] | None = None
    constituent_id: list[str] | None = None
    custom_field_category: list[str] | None = None
    fields: list[str] | None = None
    fundraiser_status: list[str] | None = None
    include_deceased: bool | None = None
    include_inactive: bool | None = None
    list_id: str | None = None
    postal_code: list[str] | None = None
    date_added: datetime | None = None
    last_modified: datetime | None = None
    sort_token: str | None = None
    sort: list[str] | None = None
    limit: Union[Annotated[int, Field(ge=1, le=5000)], None] = None
    offset: int | None = None


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


class PostResponse(BaseModel):
    id: str | None = None


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


class NameFormat(BaseModel):
    id: str | None = None
    configuration_id: str | None = None
    constituent_id: str | None = None
    custom_format: bool | None = None
    formatted_name: str | None = None
    primary_type: str | None = None


class NameFormatEdit(BaseModel):
    configuration_id: str | None = None
    custom_format: bool | None = None
    formatted_name: str | None = None
    type: str


class PrimaryNameFormat(BaseModel):
    id: str | None = None
    configuration_id: str | None = None
    constituent_id: str | None = None
    custom_format: bool | None = None
    formatted_name: str | None = None
    type: str | None = None


class PrimaryNameFormatEdit(BaseModel):
    configuration_id: str | None = None
    custom_format: bool | None = None
    formatted_name: str | None = None


class NameFormatSummary(BaseModel):
    additional_name_formats: list[NameFormat] | None = None
    primary_addressee: PrimaryNameFormat | None = None
    primary_salutation: PrimaryNameFormat | None = None


class NewDocumentInfo(BaseModel):
    file_name: str | None = None
    upload_thumbnail: bool = False


class Header(BaseModel):
    name: str | None = None
    value: str | None = None


class RequestMetaData(BaseModel):
    headers: list[Header]
    method: HttpMethods
    url: str


class FileDefinition(BaseModel):
    file_id: str | None = None
    file_upload_request: RequestMetaData
    thumbnail_id: str | None = None
    thumbnail_upload_request: RequestMetaData | None = None

    # TODO: This does not handle thumbnails at all.
    # FIXME: We don't handle the content type header.
    def upload_binary(self, data: str, content_type: ContentType) -> Response:
        self.file_upload_request.headers.append(
            Header(name="Content-Type", value=content_type)
        )
        return api_request(
            method=self.file_upload_request.method,
            url=self.file_upload_request.url,
            headers=self.file_upload_request.headers,
            data=data,
            drop_headers=True,
        )


class CollectionOfAddresses(Collection[Address]):
    pass


class CollectionOfConstituents(Collection[Constituent]):
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


def address_patch(address: Address) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/addresses/{address.id}",
        data=address.model_dump_json(exclude_none=False),
    )


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


def attachment_post(attachment: Attachment) -> PostResponse | Response:
    return api_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/constituents/attachments",
        data=attachment.model_dump_json(exclude_none=True),
        response_model=PostResponse,
    )


def constituent_get(constituent_id: str) -> Constituent | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}",
        response_model=Constituent,
    )


def constituent_list_get(
    query: ConstituentListQuery,
) -> CollectionOfConstituents | Response:
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/constituents",
        params=query.model_dump(exclude_none=True),
        response_model=CollectionOfConstituents,
    )


def constituent_search_get(
    query: ConstituentSearchQuery,
) -> CollectionOfConstituentSearchResults | Response:
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/constituents/search",
        response_model=CollectionOfConstituentSearchResults,
        params=query.model_dump(exclude_none=True),
    )


def constituent_patch(constituent: Constituent) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent.id}",
        data=constituent.model_dump_json(exclude_none=False),
    )


def document_post(request: NewDocumentInfo) -> FileDefinition | Response:
    return api_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/constituent/v1/documents",
        data=request.model_dump_json(exclude_none=True),
        response_model=FileDefinition,
    )


def email_list_all_get(**kwargs) -> CollectionOfEmails | Response:
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/constituent/v1/emailaddresses",
        response_model=CollectionOfEmails,
        **kwargs,
    )


def email_list_constituent_get(
    constituent_id: str, include_inactive: bool = False
) -> CollectionOfEmails | Response:
    url = f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/emailaddresses"
    if include_inactive:
        url = f"{url}?include_inactive=true"
    return api_request(
        method=HttpMethods.GET,
        url=url,
        response_model=CollectionOfEmails,
    )


def email_patch(email: Email) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email.id}",
        data=email.model_dump_json(exclude_none=False),
    )


def email_delete(email: Email) -> Response:
    return api_request(
        method=HttpMethods.DELETE,
        url=f"https://api.sky.blackbaud.com/constituent/v1/emailaddresses/{email.id}",
    )


def phone_list_constituent_get(
    constituent_id: str,
) -> CollectionOfPhones | Response:
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
        data=alias.model_dump_json(
            exclude_none=False, exclude={"id", "constituent_id"}
        ),
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
            exclude_none=False, exclude={"id", "constituent_id"}
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


def name_format_get(name_format_id: str) -> NameFormat | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/nameformats/{name_format_id}",
        response_model=NameFormat,
    )


def name_format_patch(name_format_id: str, name: NameFormatEdit) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/nameformats/{name_format_id}",
        data=name.model_dump_json(exclude_none=False),
    )


def name_format_primary_patch(
    primary_name_format_id: str, name: PrimaryNameFormatEdit
) -> Response:
    return api_request(
        method=HttpMethods.PATCH,
        url=f"https://api.sky.blackbaud.com/constituent/v1/primarynameformats/{primary_name_format_id}",
        data=name.model_dump_json(exclude_none=False),
    )


def name_format_summary_get(
    constituent_id: str,
) -> NameFormatSummary | Response:
    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/constituent/v1/constituents/{constituent_id}/nameformats/summary",
        response_model=NameFormatSummary,
    )
