from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.constituent_add_receipt_type import ConstituentAddReceiptType
from ..models.constituent_add_type import ConstituentAddType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constituent_address_add import ConstituentAddressAdd
    from ..models.constituent_email_address_add import ConstituentEmailAddressAdd
    from ..models.constituent_online_presence_add import ConstituentOnlinePresenceAdd
    from ..models.constituent_phone_add import ConstituentPhoneAdd
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate
    from ..models.primary_name_format_edit import PrimaryNameFormatEdit


T = TypeVar("T", bound="ConstituentAdd")


@_attrs_define
class ConstituentAdd:
    """Constituents are the individuals and organizations who support your organization by contributing time, money, and
    resources. The constituent entity stores information about donors, prospects, volunteers, general supporters, and
    more.

        Attributes:
            type_ (ConstituentAddType): The type of constituent. Available values are <i>Individual</i> and
                <i>Organization</i>.
            address (ConstituentAddressAdd | Unset): Defines the shape of an address for adding with a constituent.
            birthdate (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            deceased (bool | Unset): Indicates whether the constituent is deceased. For individuals only.
            deceased_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            email (ConstituentEmailAddressAdd | Unset): Defines the shape of an email address for adding with a constituent.
            first (str | Unset): The constituent's first name. For individuals only. Character limit: 50.
            former_name (str | Unset): The constituent's former name. For individuals only. Character limit: 100.
            gender (str | Unset): The constituent's gender. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListGenders"><b>Gender</b></a> table.
                This property defaults to <i>Unknown</i> if no value is provided. For individuals only.
            gives_anonymously (bool | Unset): Indicates whether the constituent gives anonymously.
            inactive (bool | Unset): Indicates whether the constituent is inactive.
            last (str | Unset): The constituent's last name. For individuals only (required). Character limit: 100.
            lookup_id (str | Unset): The user-defined identifier for the constituent.
            marital_status (str | Unset): The constituent's marital status. Available values are the entries in the <a href=
                "https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListMaritalStatuses"><b>M
                arital Status</b></a> table.  For individuals only.
            middle (str | Unset): The constituent's middle name. For individuals only. Character limit: 50.
            name (str | Unset): If the constituent's <code>type</code> is <i>Individual</i>, this is a computed field that
                does not apply to add operations. If the <code>type</code> is <i>Organization</i>, this field is required and
                represents the organization's name. Character limit: 60.
            online_presence (ConstituentOnlinePresenceAdd | Unset): Defines the shape of an online presence for adding with
                a constituent.
            phone (ConstituentPhoneAdd | Unset): Defines the shape of a phone for adding with a constituent.
            preferred_name (str | Unset): The constituent's preferred name. For individuals only. Character limit: 50.
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
            primary_addressee (PrimaryNameFormatEdit | Unset): Primary name formats are elevated name formats used for the
                constituent's most commonly used addressee and salutation name formats.
            primary_salutation (PrimaryNameFormatEdit | Unset): Primary name formats are elevated name formats used for the
                constituent's most commonly used addressee and salutation name formats.
            birthplace (str | Unset): The birthplace of the constituent. For individuals only.
            ethnicity (str | Unset): The ethnicity of the constituent. For individuals only.
            income (str | Unset): The income for the constituent. For individuals only.
            religion (str | Unset): The religion of the constituent. For individuals only.
            industry (str | Unset): The industry of the constituent. For organizations only.
            matches_gifts (bool | Unset): Indicates if the constituent matches gifts. For organizations only.
            matching_gift_per_gift_min (Currency | Unset): For consistency, currency is configured at the organization
                level. This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            matching_gift_per_gift_max (Currency | Unset): For consistency, currency is configured at the organization
                level. This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            matching_gift_total_min (Currency | Unset): For consistency, currency is configured at the organization level.
                This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            matching_gift_total_max (Currency | Unset): For consistency, currency is configured at the organization level.
                This ensures that all monetary amounts are consistent, regardless of where they are entered or viewed.
            matching_gift_factor (float | Unset): The matching gift factor for the constituent. For organizations only.
            matching_gift_notes (str | Unset): The matching gift notes for the constituent. For organizations only.
            num_employees (int | Unset): The number of employees for the constituent. For organizations only.
            is_memorial (bool | Unset): Indicates whether the constituent is for honor/memorial.
            is_solicitor (bool | Unset): Indicates whether the constituent is a solicitor.
            no_valid_address (bool | Unset): Indicates whether the constituent does not have a valid address.
            receipt_type (ConstituentAddReceiptType | Unset): The receipt type of the constituent.
            target (str | Unset): The target of the constituent.
            date_added (datetime.datetime | Unset): Optional.  The date the constituent was added. Useful when importing
                records from another system and the source system has a date added. Uses <a
                href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43</i>.
            requests_no_email (bool | Unset): Indicates whether the constituent requests no email.
            import_id (str | Unset): The import ID associated with the constituent. Maximum length is 20 characters.
    """

    type_: ConstituentAddType
    address: ConstituentAddressAdd | Unset = UNSET
    birthdate: FuzzyDate | Unset = UNSET
    deceased: bool | Unset = UNSET
    deceased_date: FuzzyDate | Unset = UNSET
    email: ConstituentEmailAddressAdd | Unset = UNSET
    first: str | Unset = UNSET
    former_name: str | Unset = UNSET
    gender: str | Unset = UNSET
    gives_anonymously: bool | Unset = UNSET
    inactive: bool | Unset = UNSET
    last: str | Unset = UNSET
    lookup_id: str | Unset = UNSET
    marital_status: str | Unset = UNSET
    middle: str | Unset = UNSET
    name: str | Unset = UNSET
    online_presence: ConstituentOnlinePresenceAdd | Unset = UNSET
    phone: ConstituentPhoneAdd | Unset = UNSET
    preferred_name: str | Unset = UNSET
    suffix: str | Unset = UNSET
    suffix_2: str | Unset = UNSET
    title: str | Unset = UNSET
    title_2: str | Unset = UNSET
    primary_addressee: PrimaryNameFormatEdit | Unset = UNSET
    primary_salutation: PrimaryNameFormatEdit | Unset = UNSET
    birthplace: str | Unset = UNSET
    ethnicity: str | Unset = UNSET
    income: str | Unset = UNSET
    religion: str | Unset = UNSET
    industry: str | Unset = UNSET
    matches_gifts: bool | Unset = UNSET
    matching_gift_per_gift_min: Currency | Unset = UNSET
    matching_gift_per_gift_max: Currency | Unset = UNSET
    matching_gift_total_min: Currency | Unset = UNSET
    matching_gift_total_max: Currency | Unset = UNSET
    matching_gift_factor: float | Unset = UNSET
    matching_gift_notes: str | Unset = UNSET
    num_employees: int | Unset = UNSET
    is_memorial: bool | Unset = UNSET
    is_solicitor: bool | Unset = UNSET
    no_valid_address: bool | Unset = UNSET
    receipt_type: ConstituentAddReceiptType | Unset = UNSET
    target: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    requests_no_email: bool | Unset = UNSET
    import_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        address: dict[str, Any] | Unset = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        birthdate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.birthdate, Unset):
            birthdate = self.birthdate.to_dict()

        deceased = self.deceased

        deceased_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deceased_date, Unset):
            deceased_date = self.deceased_date.to_dict()

        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        first = self.first

        former_name = self.former_name

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

        suffix = self.suffix

        suffix_2 = self.suffix_2

        title = self.title

        title_2 = self.title_2

        primary_addressee: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_addressee, Unset):
            primary_addressee = self.primary_addressee.to_dict()

        primary_salutation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_salutation, Unset):
            primary_salutation = self.primary_salutation.to_dict()

        birthplace = self.birthplace

        ethnicity = self.ethnicity

        income = self.income

        religion = self.religion

        industry = self.industry

        matches_gifts = self.matches_gifts

        matching_gift_per_gift_min: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching_gift_per_gift_min, Unset):
            matching_gift_per_gift_min = self.matching_gift_per_gift_min.to_dict()

        matching_gift_per_gift_max: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching_gift_per_gift_max, Unset):
            matching_gift_per_gift_max = self.matching_gift_per_gift_max.to_dict()

        matching_gift_total_min: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching_gift_total_min, Unset):
            matching_gift_total_min = self.matching_gift_total_min.to_dict()

        matching_gift_total_max: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matching_gift_total_max, Unset):
            matching_gift_total_max = self.matching_gift_total_max.to_dict()

        matching_gift_factor = self.matching_gift_factor

        matching_gift_notes = self.matching_gift_notes

        num_employees = self.num_employees

        is_memorial = self.is_memorial

        is_solicitor = self.is_solicitor

        no_valid_address = self.no_valid_address

        receipt_type: str | Unset = UNSET
        if not isinstance(self.receipt_type, Unset):
            receipt_type = self.receipt_type.value

        target = self.target

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        requests_no_email = self.requests_no_email

        import_id = self.import_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if address is not UNSET:
            field_dict["address"] = address
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
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
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if suffix_2 is not UNSET:
            field_dict["suffix_2"] = suffix_2
        if title is not UNSET:
            field_dict["title"] = title
        if title_2 is not UNSET:
            field_dict["title_2"] = title_2
        if primary_addressee is not UNSET:
            field_dict["primary_addressee"] = primary_addressee
        if primary_salutation is not UNSET:
            field_dict["primary_salutation"] = primary_salutation
        if birthplace is not UNSET:
            field_dict["birthplace"] = birthplace
        if ethnicity is not UNSET:
            field_dict["ethnicity"] = ethnicity
        if income is not UNSET:
            field_dict["income"] = income
        if religion is not UNSET:
            field_dict["religion"] = religion
        if industry is not UNSET:
            field_dict["industry"] = industry
        if matches_gifts is not UNSET:
            field_dict["matches_gifts"] = matches_gifts
        if matching_gift_per_gift_min is not UNSET:
            field_dict["matching_gift_per_gift_min"] = matching_gift_per_gift_min
        if matching_gift_per_gift_max is not UNSET:
            field_dict["matching_gift_per_gift_max"] = matching_gift_per_gift_max
        if matching_gift_total_min is not UNSET:
            field_dict["matching_gift_total_min"] = matching_gift_total_min
        if matching_gift_total_max is not UNSET:
            field_dict["matching_gift_total_max"] = matching_gift_total_max
        if matching_gift_factor is not UNSET:
            field_dict["matching_gift_factor"] = matching_gift_factor
        if matching_gift_notes is not UNSET:
            field_dict["matching_gift_notes"] = matching_gift_notes
        if num_employees is not UNSET:
            field_dict["num_employees"] = num_employees
        if is_memorial is not UNSET:
            field_dict["is_memorial"] = is_memorial
        if is_solicitor is not UNSET:
            field_dict["is_solicitor"] = is_solicitor
        if no_valid_address is not UNSET:
            field_dict["no_valid_address"] = no_valid_address
        if receipt_type is not UNSET:
            field_dict["receipt_type"] = receipt_type
        if target is not UNSET:
            field_dict["target"] = target
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if requests_no_email is not UNSET:
            field_dict["requests_no_email"] = requests_no_email
        if import_id is not UNSET:
            field_dict["import_id"] = import_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constituent_address_add import ConstituentAddressAdd
        from ..models.constituent_email_address_add import ConstituentEmailAddressAdd
        from ..models.constituent_online_presence_add import ConstituentOnlinePresenceAdd
        from ..models.constituent_phone_add import ConstituentPhoneAdd
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate
        from ..models.primary_name_format_edit import PrimaryNameFormatEdit

        d = dict(src_dict)
        type_ = ConstituentAddType(d.pop("type"))

        _address = d.pop("address", UNSET)
        address: ConstituentAddressAdd | Unset
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = ConstituentAddressAdd.from_dict(_address)

        _birthdate = d.pop("birthdate", UNSET)
        birthdate: FuzzyDate | Unset
        if isinstance(_birthdate, Unset):
            birthdate = UNSET
        else:
            birthdate = FuzzyDate.from_dict(_birthdate)

        deceased = d.pop("deceased", UNSET)

        _deceased_date = d.pop("deceased_date", UNSET)
        deceased_date: FuzzyDate | Unset
        if isinstance(_deceased_date, Unset):
            deceased_date = UNSET
        else:
            deceased_date = FuzzyDate.from_dict(_deceased_date)

        _email = d.pop("email", UNSET)
        email: ConstituentEmailAddressAdd | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = ConstituentEmailAddressAdd.from_dict(_email)

        first = d.pop("first", UNSET)

        former_name = d.pop("former_name", UNSET)

        gender = d.pop("gender", UNSET)

        gives_anonymously = d.pop("gives_anonymously", UNSET)

        inactive = d.pop("inactive", UNSET)

        last = d.pop("last", UNSET)

        lookup_id = d.pop("lookup_id", UNSET)

        marital_status = d.pop("marital_status", UNSET)

        middle = d.pop("middle", UNSET)

        name = d.pop("name", UNSET)

        _online_presence = d.pop("online_presence", UNSET)
        online_presence: ConstituentOnlinePresenceAdd | Unset
        if isinstance(_online_presence, Unset):
            online_presence = UNSET
        else:
            online_presence = ConstituentOnlinePresenceAdd.from_dict(_online_presence)

        _phone = d.pop("phone", UNSET)
        phone: ConstituentPhoneAdd | Unset
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = ConstituentPhoneAdd.from_dict(_phone)

        preferred_name = d.pop("preferred_name", UNSET)

        suffix = d.pop("suffix", UNSET)

        suffix_2 = d.pop("suffix_2", UNSET)

        title = d.pop("title", UNSET)

        title_2 = d.pop("title_2", UNSET)

        _primary_addressee = d.pop("primary_addressee", UNSET)
        primary_addressee: PrimaryNameFormatEdit | Unset
        if isinstance(_primary_addressee, Unset):
            primary_addressee = UNSET
        else:
            primary_addressee = PrimaryNameFormatEdit.from_dict(_primary_addressee)

        _primary_salutation = d.pop("primary_salutation", UNSET)
        primary_salutation: PrimaryNameFormatEdit | Unset
        if isinstance(_primary_salutation, Unset):
            primary_salutation = UNSET
        else:
            primary_salutation = PrimaryNameFormatEdit.from_dict(_primary_salutation)

        birthplace = d.pop("birthplace", UNSET)

        ethnicity = d.pop("ethnicity", UNSET)

        income = d.pop("income", UNSET)

        religion = d.pop("religion", UNSET)

        industry = d.pop("industry", UNSET)

        matches_gifts = d.pop("matches_gifts", UNSET)

        _matching_gift_per_gift_min = d.pop("matching_gift_per_gift_min", UNSET)
        matching_gift_per_gift_min: Currency | Unset
        if isinstance(_matching_gift_per_gift_min, Unset):
            matching_gift_per_gift_min = UNSET
        else:
            matching_gift_per_gift_min = Currency.from_dict(_matching_gift_per_gift_min)

        _matching_gift_per_gift_max = d.pop("matching_gift_per_gift_max", UNSET)
        matching_gift_per_gift_max: Currency | Unset
        if isinstance(_matching_gift_per_gift_max, Unset):
            matching_gift_per_gift_max = UNSET
        else:
            matching_gift_per_gift_max = Currency.from_dict(_matching_gift_per_gift_max)

        _matching_gift_total_min = d.pop("matching_gift_total_min", UNSET)
        matching_gift_total_min: Currency | Unset
        if isinstance(_matching_gift_total_min, Unset):
            matching_gift_total_min = UNSET
        else:
            matching_gift_total_min = Currency.from_dict(_matching_gift_total_min)

        _matching_gift_total_max = d.pop("matching_gift_total_max", UNSET)
        matching_gift_total_max: Currency | Unset
        if isinstance(_matching_gift_total_max, Unset):
            matching_gift_total_max = UNSET
        else:
            matching_gift_total_max = Currency.from_dict(_matching_gift_total_max)

        matching_gift_factor = d.pop("matching_gift_factor", UNSET)

        matching_gift_notes = d.pop("matching_gift_notes", UNSET)

        num_employees = d.pop("num_employees", UNSET)

        is_memorial = d.pop("is_memorial", UNSET)

        is_solicitor = d.pop("is_solicitor", UNSET)

        no_valid_address = d.pop("no_valid_address", UNSET)

        _receipt_type = d.pop("receipt_type", UNSET)
        receipt_type: ConstituentAddReceiptType | Unset
        if isinstance(_receipt_type, Unset):
            receipt_type = UNSET
        else:
            receipt_type = ConstituentAddReceiptType(_receipt_type)

        target = d.pop("target", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        requests_no_email = d.pop("requests_no_email", UNSET)

        import_id = d.pop("import_id", UNSET)

        constituent_add = cls(
            type_=type_,
            address=address,
            birthdate=birthdate,
            deceased=deceased,
            deceased_date=deceased_date,
            email=email,
            first=first,
            former_name=former_name,
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
            suffix=suffix,
            suffix_2=suffix_2,
            title=title,
            title_2=title_2,
            primary_addressee=primary_addressee,
            primary_salutation=primary_salutation,
            birthplace=birthplace,
            ethnicity=ethnicity,
            income=income,
            religion=religion,
            industry=industry,
            matches_gifts=matches_gifts,
            matching_gift_per_gift_min=matching_gift_per_gift_min,
            matching_gift_per_gift_max=matching_gift_per_gift_max,
            matching_gift_total_min=matching_gift_total_min,
            matching_gift_total_max=matching_gift_total_max,
            matching_gift_factor=matching_gift_factor,
            matching_gift_notes=matching_gift_notes,
            num_employees=num_employees,
            is_memorial=is_memorial,
            is_solicitor=is_solicitor,
            no_valid_address=no_valid_address,
            receipt_type=receipt_type,
            target=target,
            date_added=date_added,
            requests_no_email=requests_no_email,
            import_id=import_id,
        )

        constituent_add.additional_properties = d
        return constituent_add

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
