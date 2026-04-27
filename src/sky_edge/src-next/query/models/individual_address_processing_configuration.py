from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.address_processing_date_range import AddressProcessingDateRange
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_processing_filter import AddressProcessingFilter
    from ..models.address_type_or_enum import AddressTypeOrEnum


T = TypeVar("T", bound="IndividualAddressProcessingConfiguration")


@_attrs_define
class IndividualAddressProcessingConfiguration:
    """Address options used to determine if and which address should be printed for an individual.

    Attributes:
        default_specific_address_type_or_enum (AddressTypeOrEnum | Unset): Denotes which address to use for the address
            processing when one isn't found.
            If the Enum is SpecificAddressType, then the SpecificAddressTypeId is used.
        check_seasonal_compare_date (datetime.datetime | None | Unset): Null unless Date range is set to a specific date
            value.
            Used to compare against the Seasonal dates of address values if CheckSeasonalDateRangeType is set to
            SpecificDate
        check_seasonal_date_range_type (AddressProcessingDateRange | Unset): RE7 Date range enum<p>Members:</p><ul><li><
            i>AllDates</i></li><li><i>Today</i></li><li><i>Yesterday</i></li><li><i>Tomorrow</i></li><li><i>SpecificDate</i>
            </li><li><i>LastDayOfThisWeek</i></li><li><i>LastDayOfLastWeek</i></li><li><i>LastDayOfNextWeek</i></li><li><i>L
            astDayOfThisMonth</i></li><li><i>LastDayOfLastMonth</i></li><li><i>LastDayOfNextMonth</i></li><li><i>LastDayOfTh
            isQuarter</i></li><li><i>LastDayOfLastQuarter</i></li><li><i>LastDayOfNextQuarter</i></li><li><i>LastDayOfThisCa
            lendarYear</i></li><li><i>LastDayOfLastCalendarYear</i></li><li><i>LastDayOfNextCalendarYear</i></li><li><i>Last
            DayOfThisFiscalYear</i></li><li><i>LastDayOfLastFiscalYear</i></li><li><i>LastDayOfNextFiscalYear</i></li></ul>
        filter_collection (list[AddressProcessingFilter] | None | Unset): The collection of address filters for the
            criteria
    """

    default_specific_address_type_or_enum: AddressTypeOrEnum | Unset = UNSET
    check_seasonal_compare_date: datetime.datetime | None | Unset = UNSET
    check_seasonal_date_range_type: AddressProcessingDateRange | Unset = UNSET
    filter_collection: list[AddressProcessingFilter] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        default_specific_address_type_or_enum: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_specific_address_type_or_enum, Unset):
            default_specific_address_type_or_enum = self.default_specific_address_type_or_enum.to_dict()

        check_seasonal_compare_date: None | str | Unset
        if isinstance(self.check_seasonal_compare_date, Unset):
            check_seasonal_compare_date = UNSET
        elif isinstance(self.check_seasonal_compare_date, datetime.datetime):
            check_seasonal_compare_date = self.check_seasonal_compare_date.isoformat()
        else:
            check_seasonal_compare_date = self.check_seasonal_compare_date

        check_seasonal_date_range_type: str | Unset = UNSET
        if not isinstance(self.check_seasonal_date_range_type, Unset):
            check_seasonal_date_range_type = self.check_seasonal_date_range_type.value

        filter_collection: list[dict[str, Any]] | None | Unset
        if isinstance(self.filter_collection, Unset):
            filter_collection = UNSET
        elif isinstance(self.filter_collection, list):
            filter_collection = []
            for filter_collection_type_0_item_data in self.filter_collection:
                filter_collection_type_0_item = filter_collection_type_0_item_data.to_dict()
                filter_collection.append(filter_collection_type_0_item)

        else:
            filter_collection = self.filter_collection

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if default_specific_address_type_or_enum is not UNSET:
            field_dict["default_specific_address_type_or_enum"] = default_specific_address_type_or_enum
        if check_seasonal_compare_date is not UNSET:
            field_dict["check_seasonal_compare_date"] = check_seasonal_compare_date
        if check_seasonal_date_range_type is not UNSET:
            field_dict["check_seasonal_date_range_type"] = check_seasonal_date_range_type
        if filter_collection is not UNSET:
            field_dict["filter_collection"] = filter_collection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_processing_filter import AddressProcessingFilter
        from ..models.address_type_or_enum import AddressTypeOrEnum

        d = dict(src_dict)
        _default_specific_address_type_or_enum = d.pop("default_specific_address_type_or_enum", UNSET)
        default_specific_address_type_or_enum: AddressTypeOrEnum | Unset
        if isinstance(_default_specific_address_type_or_enum, Unset):
            default_specific_address_type_or_enum = UNSET
        else:
            default_specific_address_type_or_enum = AddressTypeOrEnum.from_dict(_default_specific_address_type_or_enum)

        def _parse_check_seasonal_compare_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                check_seasonal_compare_date_type_0 = isoparse(data)

                return check_seasonal_compare_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        check_seasonal_compare_date = _parse_check_seasonal_compare_date(d.pop("check_seasonal_compare_date", UNSET))

        _check_seasonal_date_range_type = d.pop("check_seasonal_date_range_type", UNSET)
        check_seasonal_date_range_type: AddressProcessingDateRange | Unset
        if isinstance(_check_seasonal_date_range_type, Unset):
            check_seasonal_date_range_type = UNSET
        else:
            check_seasonal_date_range_type = AddressProcessingDateRange(_check_seasonal_date_range_type)

        def _parse_filter_collection(data: object) -> list[AddressProcessingFilter] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                filter_collection_type_0 = []
                _filter_collection_type_0 = data
                for filter_collection_type_0_item_data in _filter_collection_type_0:
                    filter_collection_type_0_item = AddressProcessingFilter.from_dict(
                        filter_collection_type_0_item_data
                    )

                    filter_collection_type_0.append(filter_collection_type_0_item)

                return filter_collection_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[AddressProcessingFilter] | None | Unset, data)

        filter_collection = _parse_filter_collection(d.pop("filter_collection", UNSET))

        individual_address_processing_configuration = cls(
            default_specific_address_type_or_enum=default_specific_address_type_or_enum,
            check_seasonal_compare_date=check_seasonal_compare_date,
            check_seasonal_date_range_type=check_seasonal_date_range_type,
            filter_collection=filter_collection,
        )

        return individual_address_processing_configuration
