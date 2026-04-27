from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

from ..models.non_constituent_add_type import NonConstituentAddType

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate
    from ..models.primary_name_format_edit import PrimaryNameFormatEdit


T = TypeVar("T", bound="NonConstituentAdd")


@_attrs_define
class NonConstituentAdd:
    """Non-constituents are the individuals and organizations related to constituents.

    Attributes:
        type_ (NonConstituentAddType): The type of constituent. Available values are <i>Individual</i> and
            <i>Organization</i>.
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
        last (str | Unset): The constituent's last name. For individuals only (required). Character limit: 100.
        middle (str | Unset): The constituent's middle name. For individuals only. Character limit: 50.
        name (str | Unset): If the constituent's <code>type</code> is <i>Individual</i>, this is a computed field that
            does not apply to add operations. If the <code>type</code> is <i>Organization</i>, this field is required and
            represents the organization's name. Character limit: 60.
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
    """

    type_: NonConstituentAddType
    birthdate: FuzzyDate | Unset = UNSET
    deceased: bool | Unset = UNSET
    deceased_date: FuzzyDate | Unset = UNSET
    first: str | Unset = UNSET
    former_name: str | Unset = UNSET
    gender: str | Unset = UNSET
    last: str | Unset = UNSET
    middle: str | Unset = UNSET
    name: str | Unset = UNSET
    preferred_name: str | Unset = UNSET
    suffix: str | Unset = UNSET
    suffix_2: str | Unset = UNSET
    title: str | Unset = UNSET
    title_2: str | Unset = UNSET
    primary_addressee: PrimaryNameFormatEdit | Unset = UNSET
    primary_salutation: PrimaryNameFormatEdit | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

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

        last = self.last

        middle = self.middle

        name = self.name

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
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
        if last is not UNSET:
            field_dict["last"] = last
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
        if primary_addressee is not UNSET:
            field_dict["primary_addressee"] = primary_addressee
        if primary_salutation is not UNSET:
            field_dict["primary_salutation"] = primary_salutation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate
        from ..models.primary_name_format_edit import PrimaryNameFormatEdit

        d = dict(src_dict)
        type_ = NonConstituentAddType(d.pop("type"))

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

        last = d.pop("last", UNSET)

        middle = d.pop("middle", UNSET)

        name = d.pop("name", UNSET)

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

        non_constituent_add = cls(
            type_=type_,
            birthdate=birthdate,
            deceased=deceased,
            deceased_date=deceased_date,
            first=first,
            former_name=former_name,
            gender=gender,
            last=last,
            middle=middle,
            name=name,
            preferred_name=preferred_name,
            suffix=suffix,
            suffix_2=suffix_2,
            title=title,
            title_2=title_2,
            primary_addressee=primary_addressee,
            primary_salutation=primary_salutation,
        )

        non_constituent_add.additional_properties = d
        return non_constituent_add

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
