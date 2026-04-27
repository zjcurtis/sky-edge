from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.constituent_list_item_fundraiser_status import ConstituentListItemFundraiserStatus
from ..models.constituent_list_item_type import ConstituentListItemType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_read import AddressRead
    from ..models.constituent_assigned_fundraiser import ConstituentAssignedFundraiser
    from ..models.email_address_read import EmailAddressRead
    from ..models.fuzzy_date import FuzzyDate
    from ..models.online_presence_read import OnlinePresenceRead
    from ..models.phone_read import PhoneRead
    from ..models.spouse_read import SpouseRead


T = TypeVar("T", bound="ConstituentListItem")


@_attrs_define
class ConstituentListItem:
    """Constituents are the individuals and organizations who support your organization by contributing time, money, and
    resources. The constituent entity stores information about donors, prospects, volunteers, general supporters, and
    more.

        Attributes:
            id (str | Unset): The immutable system record ID for the constituent. This is not the same as the user-definable
                constituent identifier, which is stored in the <code>lookup_id</code>.
            address (AddressRead | Unset): Addresses store information about constituent residences and other addresses
                along with information about where or whether to send mail.
            age (int | Unset): This computed field calculates the constituent's age based on the <code>birthdate</code>
                property. For individuals only.
            birthdate (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            date_added (datetime.datetime | Unset): The date when the constituent was created. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the constituent was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            deceased (bool | Unset): Indicates whether the constituent is deceased. For individuals only.
            deceased_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            email (EmailAddressRead | Unset): Email addresses store information about constituent email accounts and where
                to send email correspondences for individuals and organizations.
            first (str | Unset): The constituent's first name. For individuals only.
            former_name (str | Unset): The constituent's former name. For individuals only.
            fundraiser_status (ConstituentListItemFundraiserStatus | Unset): Indicates whether the constituent is a
                fundraiser. For individuals only.
            constituent_assigned_fundraisers (list[ConstituentAssignedFundraiser] | Unset): The active fundraisers assigned
                to the constituent.
            gender (str | Unset): The constituent's gender. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListGenders"><b>Gender</b></a> table.
                This property defaults to <i>unknown</i> if no value is provided. For individuals only.
            gives_anonymously (bool | Unset): Indicates whether the constituent gives anonymously.
            inactive (bool | Unset): Indicates whether the constituent is inactive.
            last (str | Unset): The constituent's last name. For individuals only.
            lookup_id (str | Unset): The user-defined identifier for the constituent.
            marital_status (str | Unset): The constituent's marital status. Available values are the entries in the <a href=
                "https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListMaritalStatuses"><b>M
                arital Status</b></a> table.  For individuals only.
            middle (str | Unset): The constituent's middle name. For individuals only.
            name (str | Unset): If the constituent's <code>type</code> is <i>Individual</i>, this computed field indicates
                the full name of the constituent based on the target organization’s display name settings. If the
                <code>type</code> is <i>Organization</i>, this is the organization's name.
            online_presence (OnlinePresenceRead | Unset): Online presence entities store a constituent’s social media
                accounts, websites, and other means of reaching out or gaining more information about the constituent.
            phone (PhoneRead | Unset): Phones store information about constituent phone numbers and where to call
                individuals and organizations.
            preferred_name (str | Unset): The constituent's preferred name. For individuals only.
            spouse (SpouseRead | Unset): The spouse entity describes spouses for individual constituents.
            suffix (str | Unset): The constituent's primary suffix. Available values are the entries in the <a href="https:/
                /developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListSuffixes"><b>Suffixes</b></a>
                table. For individuals only.
            suffix_2 (str | Unset): The constituent's secondary suffix. Available values are the entries in the <a href="htt
                ps://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListSuffixes"><b>Suffixes</b>
                </a> table. For individuals only.
            title (str | Unset): The constituent's primary title. Available values are the entries in the <a href="https://d
                eveloper.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListTitles"><b>Titles</b></a>
                table. For individuals only.
            title_2 (str | Unset): The constituent's secondary title. Available values are the entries in the <a href="https
                ://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListTitles"><b>Titles</b></a>
                table. For individuals only.
            type_ (ConstituentListItemType | Unset): The type of constituent. Available values are <i>Individual</i> and
                <i>Organization</i>.
    """

    id: str | Unset = UNSET
    address: AddressRead | Unset = UNSET
    age: int | Unset = UNSET
    birthdate: FuzzyDate | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    deceased: bool | Unset = UNSET
    deceased_date: FuzzyDate | Unset = UNSET
    email: EmailAddressRead | Unset = UNSET
    first: str | Unset = UNSET
    former_name: str | Unset = UNSET
    fundraiser_status: ConstituentListItemFundraiserStatus | Unset = UNSET
    constituent_assigned_fundraisers: list[ConstituentAssignedFundraiser] | Unset = UNSET
    gender: str | Unset = UNSET
    gives_anonymously: bool | Unset = UNSET
    inactive: bool | Unset = UNSET
    last: str | Unset = UNSET
    lookup_id: str | Unset = UNSET
    marital_status: str | Unset = UNSET
    middle: str | Unset = UNSET
    name: str | Unset = UNSET
    online_presence: OnlinePresenceRead | Unset = UNSET
    phone: PhoneRead | Unset = UNSET
    preferred_name: str | Unset = UNSET
    spouse: SpouseRead | Unset = UNSET
    suffix: str | Unset = UNSET
    suffix_2: str | Unset = UNSET
    title: str | Unset = UNSET
    title_2: str | Unset = UNSET
    type_: ConstituentListItemType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        age = self.age

        birthdate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.birthdate, Unset):
            birthdate = self.birthdate.to_dict()

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        deceased = self.deceased

        deceased_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deceased_date, Unset):
            deceased_date = self.deceased_date.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        first = self.first

        former_name = self.former_name

        fundraiser_status: str | Unset = UNSET
        if not isinstance(self.fundraiser_status, Unset):
            fundraiser_status = self.fundraiser_status.value

        constituent_assigned_fundraisers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.constituent_assigned_fundraisers, Unset):
            constituent_assigned_fundraisers = []
            for constituent_assigned_fundraisers_item_data in self.constituent_assigned_fundraisers:
                constituent_assigned_fundraisers_item = constituent_assigned_fundraisers_item_data.to_dict()
                constituent_assigned_fundraisers.append(constituent_assigned_fundraisers_item)

        gender = self.gender

        gives_anonymously = self.gives_anonymously

        inactive = self.inactive

        last = self.last

        lookup_id = self.lookup_id

        marital_status = self.marital_status

        middle = self.middle

        name = self.name

        online_presence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.online_presence, Unset):
            online_presence = self.online_presence.to_dict()

        phone: dict[str, Any] | Unset = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.to_dict()

        preferred_name = self.preferred_name

        spouse: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spouse, Unset):
            spouse = self.spouse.to_dict()

        suffix = self.suffix

        suffix_2 = self.suffix_2

        title = self.title

        title_2 = self.title_2

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if age is not UNSET:
            field_dict["age"] = age
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if deceased_date is not UNSET:
            field_dict["deceased_date"] = deceased_date
        if email is not UNSET:
            field_dict["email"] = email
        if first is not UNSET:
            field_dict["first"] = first
        if former_name is not UNSET:
            field_dict["former_name"] = former_name
        if fundraiser_status is not UNSET:
            field_dict["fundraiser_status"] = fundraiser_status
        if constituent_assigned_fundraisers is not UNSET:
            field_dict["constituent_assigned_fundraisers"] = constituent_assigned_fundraisers
        if gender is not UNSET:
            field_dict["gender"] = gender
        if gives_anonymously is not UNSET:
            field_dict["gives_anonymously"] = gives_anonymously
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if last is not UNSET:
            field_dict["last"] = last
        if lookup_id is not UNSET:
            field_dict["lookup_id"] = lookup_id
        if marital_status is not UNSET:
            field_dict["marital_status"] = marital_status
        if middle is not UNSET:
            field_dict["middle"] = middle
        if name is not UNSET:
            field_dict["name"] = name
        if online_presence is not UNSET:
            field_dict["online_presence"] = online_presence
        if phone is not UNSET:
            field_dict["phone"] = phone
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if spouse is not UNSET:
            field_dict["spouse"] = spouse
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if suffix_2 is not UNSET:
            field_dict["suffix_2"] = suffix_2
        if title is not UNSET:
            field_dict["title"] = title
        if title_2 is not UNSET:
            field_dict["title_2"] = title_2
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_read import AddressRead
        from ..models.constituent_assigned_fundraiser import ConstituentAssignedFundraiser
        from ..models.email_address_read import EmailAddressRead
        from ..models.fuzzy_date import FuzzyDate
        from ..models.online_presence_read import OnlinePresenceRead
        from ..models.phone_read import PhoneRead
        from ..models.spouse_read import SpouseRead

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _address = d.pop("address", UNSET)
        address: AddressRead | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = AddressRead.from_dict(_address)

        age = d.pop("age", UNSET)

        _birthdate = d.pop("birthdate", UNSET)
        birthdate: FuzzyDate | Unset
        if isinstance(_birthdate, Unset):
            birthdate = UNSET
        else:
            birthdate = FuzzyDate.from_dict(_birthdate)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        deceased = d.pop("deceased", UNSET)

        _deceased_date = d.pop("deceased_date", UNSET)
        deceased_date: FuzzyDate | Unset
        if isinstance(_deceased_date, Unset):
            deceased_date = UNSET
        else:
            deceased_date = FuzzyDate.from_dict(_deceased_date)

        _email = d.pop("email", UNSET)
        email: EmailAddressRead | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = EmailAddressRead.from_dict(_email)

        first = d.pop("first", UNSET)

        former_name = d.pop("former_name", UNSET)

        _fundraiser_status = d.pop("fundraiser_status", UNSET)
        fundraiser_status: ConstituentListItemFundraiserStatus | Unset
        if isinstance(_fundraiser_status, Unset):
            fundraiser_status = UNSET
        else:
            fundraiser_status = ConstituentListItemFundraiserStatus(_fundraiser_status)

        _constituent_assigned_fundraisers = d.pop("constituent_assigned_fundraisers", UNSET)
        constituent_assigned_fundraisers: list[ConstituentAssignedFundraiser] | Unset = UNSET
        if _constituent_assigned_fundraisers is not UNSET:
            constituent_assigned_fundraisers = []
            for constituent_assigned_fundraisers_item_data in _constituent_assigned_fundraisers:
                constituent_assigned_fundraisers_item = ConstituentAssignedFundraiser.from_dict(
                    constituent_assigned_fundraisers_item_data
                )

                constituent_assigned_fundraisers.append(constituent_assigned_fundraisers_item)

        gender = d.pop("gender", UNSET)

        gives_anonymously = d.pop("gives_anonymously", UNSET)

        inactive = d.pop("inactive", UNSET)

        last = d.pop("last", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        marital_status = d.pop("marital_status", UNSET)

        middle = d.pop("middle", UNSET)

        name = d.pop("name", UNSET)

        _online_presence = d.pop("online_presence", UNSET)
        online_presence: OnlinePresenceRead | Unset
        if isinstance(_online_presence, Unset):
            online_presence = UNSET
        else:
            online_presence = OnlinePresenceRead.from_dict(_online_presence)

        _phone = d.pop("phone", UNSET)
        phone: PhoneRead | Unset
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = PhoneRead.from_dict(_phone)

        preferred_name = d.pop("preferred_name", UNSET)

        _spouse = d.pop("spouse", UNSET)
        spouse: SpouseRead | Unset
        if isinstance(_spouse, Unset):
            spouse = UNSET
        else:
            spouse = SpouseRead.from_dict(_spouse)

        suffix = d.pop("suffix", UNSET)

        suffix_2 = d.pop("suffix_2", UNSET)

        title = d.pop("title", UNSET)

        title_2 = d.pop("title_2", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: ConstituentListItemType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = ConstituentListItemType(_type_)

        constituent_list_item = cls(
            id=id,
            address=address,
            age=age,
            birthdate=birthdate,
            date_added=date_added,
            date_modified=date_modified,
            deceased=deceased,
            deceased_date=deceased_date,
            email=email,
            first=first,
            former_name=former_name,
            fundraiser_status=fundraiser_status,
            constituent_assigned_fundraisers=constituent_assigned_fundraisers,
            gender=gender,
            gives_anonymously=gives_anonymously,
            inactive=inactive,
            last=last,
            lookup_id=lookup_id,
            marital_status=marital_status,
            middle=middle,
            name=name,
            online_presence=online_presence,
            phone=phone,
            preferred_name=preferred_name,
            spouse=spouse,
            suffix=suffix,
            suffix_2=suffix_2,
            title=title,
            title_2=title_2,
            type_=type_,
        )

        constituent_list_item.additional_properties = d
        return constituent_list_item

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
