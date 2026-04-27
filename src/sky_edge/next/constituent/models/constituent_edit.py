from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

from ..models.constituent_edit_receipt_type import ConstituentEditReceiptType

if TYPE_CHECKING:
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="ConstituentEdit")


@_attrs_define
class ConstituentEdit:
    """Constituents are the individuals and organizations who support your organization by contributing time, money, and
    resources. The constituent entity stores information about donors, prospects, volunteers, general supporters, and
    more.

        Attributes:
            birthdate (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            deceased (bool | Unset): Indicates whether the constituent is deceased. For individuals only.
            deceased_date (FuzzyDate | Unset): Fuzzy dates provide a versatile date type to create partial dates such as
                February 9 (with no year indicated).
            first (str | Unset): The constituent's first name. For individuals only. Character limit: 50.
            former_name (str | Unset): The constituent's former name. For individuals only. Character limit: 100.
            gender (str | Unset): The constituent's gender. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListGenders"><b>Gender</b></a> table.
                This property defaults to <i>Unknown</i> if no value is provided. For individuals only.
            gives_anonymously (bool | Unset): Indicates whether the constituent gives anonymously.
            inactive (bool | Unset): Indicates whether the constituent is inactive.
            last (str | Unset): The constituent's last name. For individuals only. Character limit: 100.
            lookup_id (str | Unset): The user-defined identifier for the constituent.
            marital_status (str | Unset): The constituent's marital status. Available values are the entries in the <a href=
                "https://developer.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListMaritalStatuses"><b>M
                arital Status</b></a> table.  For individuals only.
            middle (str | Unset): The constituent's middle name. For individuals only. Character limit: 50.
            name (str | Unset): If the constituent's <code>type</code> is <i>Individual</i>, this is a computed field that
                does not apply to edit operations. If the <code>type</code> is <i>Organization</i>, this field cannot be changed
                to null and represents the organization's name. Character limit: 60.
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
            receipt_type (ConstituentEditReceiptType | Unset): The receipt type of the constituent.
            target (str | Unset): The target of the constituent.
            requests_no_email (bool | Unset): Indicates whether the constituent requests no email.
            num_subsidiaries (int | Unset): The number of subsidiaries for the constituent. For organizations only.
            parent_corporation_id (int | Unset): The parent corporation identifier of the constituent. For organizations
                only.
            parent_corporation_name (str | Unset): The parent corporation name of the constituent. For organizations only.
    """

    birthdate: FuzzyDate | Unset = UNSET
    deceased: bool | Unset = UNSET
    deceased_date: FuzzyDate | Unset = UNSET
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
    preferred_name: str | Unset = UNSET
    suffix: str | Unset = UNSET
    suffix_2: str | Unset = UNSET
    title: str | Unset = UNSET
    title_2: str | Unset = UNSET
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
    receipt_type: ConstituentEditReceiptType | Unset = UNSET
    target: str | Unset = UNSET
    requests_no_email: bool | Unset = UNSET
    num_subsidiaries: int | Unset = UNSET
    parent_corporation_id: int | Unset = UNSET
    parent_corporation_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        birthdate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.birthdate, Unset):
            birthdate = self.birthdate.to_dict()

        deceased = self.deceased

        deceased_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.deceased_date, Unset):
            deceased_date = self.deceased_date.to_dict()

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

        preferred_name = self.preferred_name

        suffix = self.suffix

        suffix_2 = self.suffix_2

        title = self.title

        title_2 = self.title_2

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

        requests_no_email = self.requests_no_email

        num_subsidiaries = self.num_subsidiaries

        parent_corporation_id = self.parent_corporation_id

        parent_corporation_name = self.parent_corporation_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if birthdate is not UNSET:
            field_dict["birthdate"] = birthdate
        if deceased is not UNSET:
            field_dict["deceased"] = deceased
        if deceased_date is not UNSET:
            field_dict["deceased_date"] = deceased_date
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
        if requests_no_email is not UNSET:
            field_dict["requests_no_email"] = requests_no_email
        if num_subsidiaries is not UNSET:
            field_dict["num_subsidiaries"] = num_subsidiaries
        if parent_corporation_id is not UNSET:
            field_dict["parent_corporation_id"] = parent_corporation_id
        if parent_corporation_name is not UNSET:
            field_dict["parent_corporation_name"] = parent_corporation_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
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

        preferred_name = d.pop("preferred_name", UNSET)

        suffix = d.pop("suffix", UNSET)

        suffix_2 = d.pop("suffix_2", UNSET)

        title = d.pop("title", UNSET)

        title_2 = d.pop("title_2", UNSET)

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
        receipt_type: ConstituentEditReceiptType | Unset
        if isinstance(_receipt_type, Unset):
            receipt_type = UNSET
        else:
            receipt_type = ConstituentEditReceiptType(_receipt_type)

        target = d.pop("target", UNSET)

        requests_no_email = d.pop("requests_no_email", UNSET)

        num_subsidiaries = d.pop("num_subsidiaries", UNSET)

        parent_corporation_id = d.pop("parent_corporation_id", UNSET)

        parent_corporation_name = d.pop("parent_corporation_name", UNSET)

        constituent_edit = cls(
            birthdate=birthdate,
            deceased=deceased,
            deceased_date=deceased_date,
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
            preferred_name=preferred_name,
            suffix=suffix,
            suffix_2=suffix_2,
            title=title,
            title_2=title_2,
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
            requests_no_email=requests_no_email,
            num_subsidiaries=num_subsidiaries,
            parent_corporation_id=parent_corporation_id,
            parent_corporation_name=parent_corporation_name,
        )

        constituent_edit.additional_properties = d
        return constituent_edit

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
