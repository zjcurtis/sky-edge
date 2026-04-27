from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="Constituent")


@_attrs_define
class Constituent:
    """Additional information about an constituent record.

    Attributes:
        record_id (int | Unset): The record id.
        constituent_id (None | str | Unset): The constituent id.
        import_id (None | str | Unset): The import id.
        is_constituent (bool | Unset): Indicates if the record is a constituent.
        is_deceased (bool | Unset): Indicates if the record is deceased.
        is_inactive (bool | Unset): Indicates if the record is inactive.
        last_name (None | str | Unset): The last name.
        first_name (None | str | Unset): The first name.
        middle_name (None | str | Unset): The middle name.
        key_indicator (None | str | Unset): The key indicator for the record.
        maiden_name (None | str | Unset): The maiden name.
        org_name (None | str | Unset): The organization name.
        gender (None | str | Unset): The gender.
        address_block (None | str | Unset): The address block.
        address_city_state (None | str | Unset): The address city and state.
        address_post_code (None | str | Unset): The address post code.
        primary_email (None | str | Unset): The primary email.
        primary_phone (None | str | Unset): The primary phone.
        title1 (None | str | Unset): The title 1.
        suffix1 (None | str | Unset): The suffix 1.
        birth_date (FuzzyDate | Unset):
        preferred_name (None | str | Unset): The preferred name.
        spouse_first_name (None | str | Unset): The spouse's first name.
        spouse_last_name (None | str | Unset): The spouse's last name.
    """

    record_id: int | Unset = UNSET
    constituent_id: None | str | Unset = UNSET
    import_id: None | str | Unset = UNSET
    is_constituent: bool | Unset = UNSET
    is_deceased: bool | Unset = UNSET
    is_inactive: bool | Unset = UNSET
    last_name: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    middle_name: None | str | Unset = UNSET
    key_indicator: None | str | Unset = UNSET
    maiden_name: None | str | Unset = UNSET
    org_name: None | str | Unset = UNSET
    gender: None | str | Unset = UNSET
    address_block: None | str | Unset = UNSET
    address_city_state: None | str | Unset = UNSET
    address_post_code: None | str | Unset = UNSET
    primary_email: None | str | Unset = UNSET
    primary_phone: None | str | Unset = UNSET
    title1: None | str | Unset = UNSET
    suffix1: None | str | Unset = UNSET
    birth_date: FuzzyDate | Unset = UNSET
    preferred_name: None | str | Unset = UNSET
    spouse_first_name: None | str | Unset = UNSET
    spouse_last_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        record_id = self.record_id

        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        is_constituent = self.is_constituent

        is_deceased = self.is_deceased

        is_inactive = self.is_inactive

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        middle_name: None | str | Unset
        if isinstance(self.middle_name, Unset):
            middle_name = UNSET
        else:
            middle_name = self.middle_name

        key_indicator: None | str | Unset
        if isinstance(self.key_indicator, Unset):
            key_indicator = UNSET
        else:
            key_indicator = self.key_indicator

        maiden_name: None | str | Unset
        if isinstance(self.maiden_name, Unset):
            maiden_name = UNSET
        else:
            maiden_name = self.maiden_name

        org_name: None | str | Unset
        if isinstance(self.org_name, Unset):
            org_name = UNSET
        else:
            org_name = self.org_name

        gender: None | str | Unset
        if isinstance(self.gender, Unset):
            gender = UNSET
        else:
            gender = self.gender

        address_block: None | str | Unset
        if isinstance(self.address_block, Unset):
            address_block = UNSET
        else:
            address_block = self.address_block

        address_city_state: None | str | Unset
        if isinstance(self.address_city_state, Unset):
            address_city_state = UNSET
        else:
            address_city_state = self.address_city_state

        address_post_code: None | str | Unset
        if isinstance(self.address_post_code, Unset):
            address_post_code = UNSET
        else:
            address_post_code = self.address_post_code

        primary_email: None | str | Unset
        if isinstance(self.primary_email, Unset):
            primary_email = UNSET
        else:
            primary_email = self.primary_email

        primary_phone: None | str | Unset
        if isinstance(self.primary_phone, Unset):
            primary_phone = UNSET
        else:
            primary_phone = self.primary_phone

        title1: None | str | Unset
        if isinstance(self.title1, Unset):
            title1 = UNSET
        else:
            title1 = self.title1

        suffix1: None | str | Unset
        if isinstance(self.suffix1, Unset):
            suffix1 = UNSET
        else:
            suffix1 = self.suffix1

        birth_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.birth_date, Unset):
            birth_date = self.birth_date.to_dict()

        preferred_name: None | str | Unset
        if isinstance(self.preferred_name, Unset):
            preferred_name = UNSET
        else:
            preferred_name = self.preferred_name

        spouse_first_name: None | str | Unset
        if isinstance(self.spouse_first_name, Unset):
            spouse_first_name = UNSET
        else:
            spouse_first_name = self.spouse_first_name

        spouse_last_name: None | str | Unset
        if isinstance(self.spouse_last_name, Unset):
            spouse_last_name = UNSET
        else:
            spouse_last_name = self.spouse_last_name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if is_constituent is not UNSET:
            field_dict["is_constituent"] = is_constituent
        if is_deceased is not UNSET:
            field_dict["is_deceased"] = is_deceased
        if is_inactive is not UNSET:
            field_dict["is_inactive"] = is_inactive
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if middle_name is not UNSET:
            field_dict["middle_name"] = middle_name
        if key_indicator is not UNSET:
            field_dict["key_indicator"] = key_indicator
        if maiden_name is not UNSET:
            field_dict["maiden_name"] = maiden_name
        if org_name is not UNSET:
            field_dict["org_name"] = org_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if address_block is not UNSET:
            field_dict["address_block"] = address_block
        if address_city_state is not UNSET:
            field_dict["address_city_state"] = address_city_state
        if address_post_code is not UNSET:
            field_dict["address_post_code"] = address_post_code
        if primary_email is not UNSET:
            field_dict["primary_email"] = primary_email
        if primary_phone is not UNSET:
            field_dict["primary_phone"] = primary_phone
        if title1 is not UNSET:
            field_dict["title1"] = title1
        if suffix1 is not UNSET:
            field_dict["suffix1"] = suffix1
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if preferred_name is not UNSET:
            field_dict["preferred_name"] = preferred_name
        if spouse_first_name is not UNSET:
            field_dict["spouse_first_name"] = spouse_first_name
        if spouse_last_name is not UNSET:
            field_dict["spouse_last_name"] = spouse_last_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)
        record_id = d.pop("record_id", UNSET)

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        is_constituent = d.pop("is_constituent", UNSET)

        is_deceased = d.pop("is_deceased", UNSET)

        is_inactive = d.pop("is_inactive", UNSET)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        def _parse_middle_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        middle_name = _parse_middle_name(d.pop("middle_name", UNSET))

        def _parse_key_indicator(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        key_indicator = _parse_key_indicator(d.pop("key_indicator", UNSET))

        def _parse_maiden_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        maiden_name = _parse_maiden_name(d.pop("maiden_name", UNSET))

        def _parse_org_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        org_name = _parse_org_name(d.pop("org_name", UNSET))

        def _parse_gender(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        gender = _parse_gender(d.pop("gender", UNSET))

        def _parse_address_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_block = _parse_address_block(d.pop("address_block", UNSET))

        def _parse_address_city_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_city_state = _parse_address_city_state(d.pop("address_city_state", UNSET))

        def _parse_address_post_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_post_code = _parse_address_post_code(d.pop("address_post_code", UNSET))

        def _parse_primary_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_email = _parse_primary_email(d.pop("primary_email", UNSET))

        def _parse_primary_phone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        primary_phone = _parse_primary_phone(d.pop("primary_phone", UNSET))

        def _parse_title1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title1 = _parse_title1(d.pop("title1", UNSET))

        def _parse_suffix1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        suffix1 = _parse_suffix1(d.pop("suffix1", UNSET))

        _birth_date = d.pop("birth_date", UNSET)
        birth_date: FuzzyDate | Unset
        if isinstance(_birth_date, Unset):
            birth_date = UNSET
        else:
            birth_date = FuzzyDate.from_dict(_birth_date)

        def _parse_preferred_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        preferred_name = _parse_preferred_name(d.pop("preferred_name", UNSET))

        def _parse_spouse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spouse_first_name = _parse_spouse_first_name(d.pop("spouse_first_name", UNSET))

        def _parse_spouse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        spouse_last_name = _parse_spouse_last_name(d.pop("spouse_last_name", UNSET))

        constituent = cls(
            record_id=record_id,
            constituent_id=constituent_id,
            import_id=import_id,
            is_constituent=is_constituent,
            is_deceased=is_deceased,
            is_inactive=is_inactive,
            last_name=last_name,
            first_name=first_name,
            middle_name=middle_name,
            key_indicator=key_indicator,
            maiden_name=maiden_name,
            org_name=org_name,
            gender=gender,
            address_block=address_block,
            address_city_state=address_city_state,
            address_post_code=address_post_code,
            primary_email=primary_email,
            primary_phone=primary_phone,
            title1=title1,
            suffix1=suffix1,
            birth_date=birth_date,
            preferred_name=preferred_name,
            spouse_first_name=spouse_first_name,
            spouse_last_name=spouse_last_name,
        )

        return constituent
