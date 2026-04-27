from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.premium_frequency import PremiumFrequency

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry
    from ..models.currency import Currency
    from ..models.fuzzy_date import FuzzyDate


T = TypeVar("T", bound="PlannedGiftRead")


@_attrs_define
class PlannedGiftRead:
    """Represents a planned gift in the API response.

    Attributes:
        id (None | str): The planned gift identifier.
        vehicle (int | None | Unset): The vehicle type (numeric).
        remainder (Currency | Unset): An amount denominated in a specific currency.
        remainder_date (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        net_present_value (Currency | Unset): An amount denominated in a specific currency.
        net_present_value_date (FuzzyDate | Unset): Expresses a date as separate Year, Month, and Day components.
        revocable (bool | None | Unset): Whether the planned gift is revocable.
            Null when the field is not applicable for the current region.
        realized (bool | Unset): Whether the planned gift is realized.
        expected_maturity_year (int | None | Unset): The expected maturity year.
        status (CodeTableEntry | Unset): A predefined entry in a code table.
        payout_percent (float | None | Unset): The payout percentage.
        payout_amount (Currency | Unset): An amount denominated in a specific currency.
        flexible_deferred (bool | None | Unset): Whether the gift annuity is flexible/deferred.
            Null when the field is not applicable for the current region.
        constituent_is_beneficiary (bool | Unset): Whether the constituent is a beneficiary.
        term_type (int | None | Unset): The term type.
        term_end_date (datetime.datetime | None | Unset): The term end date.
        trust_tax_id (None | str | Unset): The trust tax ID.
        discount_rate (float | None | Unset): The discount rate.
        payment_frequency (int | None | Unset): The payment frequency.
        first_payment_date (datetime.datetime | None | Unset): The first payment date.
        term_years (int | None | Unset): The number of years in the term.
        pooled_income_fund (CodeTableEntry | Unset): A predefined entry in a code table.
        pooled_income_fund_units (int | None | Unset): The number of pooled income fund units.
        pooled_income_fund_total_units (int | None | Unset): The total pooled income fund units.
        constituent_address_id (None | str | Unset): The constituent address identifier.
        address_block (None | str | Unset): The address block.
        address_city (None | str | Unset): The city.
        address_state (None | str | Unset): The state.
        address_post_code (None | str | Unset): The postal code.
        address_country (None | str | Unset): The country.
        constituent_is_policy_owner (bool | Unset): Whether the constituent is the policy owner.
        constituent_pays_premium (bool | Unset): Whether the constituent pays the premium.
        premium_is_fully_paid (bool | Unset): Whether the premium is fully paid.
        insurance_carrier (None | str | Unset): The insurance carrier name.
        policy_number (None | str | Unset): The policy number.
        policy_type (CodeTableEntry | Unset): A predefined entry in a code table.
        policy_face_amount (Currency | Unset): An amount denominated in a specific currency.
        premium_frequency (PremiumFrequency | Unset): Premium schedule frequency options for Life Insurance vehicles.
        premium_start_date (datetime.datetime | None | Unset): The premium schedule start date.
        premium_end_date (datetime.datetime | None | Unset): The premium schedule end date.
        premium_day_of_month (int | None | Unset): The day of month for premium payments (1-31).
        premium_month (int | None | Unset): The month for annual premium payments (1-12).
        premium_spacing (int | None | Unset): The spacing/interval for premium payments.
    """

    id: None | str
    vehicle: int | None | Unset = UNSET
    remainder: Currency | Unset = UNSET
    remainder_date: FuzzyDate | Unset = UNSET
    net_present_value: Currency | Unset = UNSET
    net_present_value_date: FuzzyDate | Unset = UNSET
    revocable: bool | None | Unset = UNSET
    realized: bool | Unset = UNSET
    expected_maturity_year: int | None | Unset = UNSET
    status: CodeTableEntry | Unset = UNSET
    payout_percent: float | None | Unset = UNSET
    payout_amount: Currency | Unset = UNSET
    flexible_deferred: bool | None | Unset = UNSET
    constituent_is_beneficiary: bool | Unset = UNSET
    term_type: int | None | Unset = UNSET
    term_end_date: datetime.datetime | None | Unset = UNSET
    trust_tax_id: None | str | Unset = UNSET
    discount_rate: float | None | Unset = UNSET
    payment_frequency: int | None | Unset = UNSET
    first_payment_date: datetime.datetime | None | Unset = UNSET
    term_years: int | None | Unset = UNSET
    pooled_income_fund: CodeTableEntry | Unset = UNSET
    pooled_income_fund_units: int | None | Unset = UNSET
    pooled_income_fund_total_units: int | None | Unset = UNSET
    constituent_address_id: None | str | Unset = UNSET
    address_block: None | str | Unset = UNSET
    address_city: None | str | Unset = UNSET
    address_state: None | str | Unset = UNSET
    address_post_code: None | str | Unset = UNSET
    address_country: None | str | Unset = UNSET
    constituent_is_policy_owner: bool | Unset = UNSET
    constituent_pays_premium: bool | Unset = UNSET
    premium_is_fully_paid: bool | Unset = UNSET
    insurance_carrier: None | str | Unset = UNSET
    policy_number: None | str | Unset = UNSET
    policy_type: CodeTableEntry | Unset = UNSET
    policy_face_amount: Currency | Unset = UNSET
    premium_frequency: PremiumFrequency | Unset = UNSET
    premium_start_date: datetime.datetime | None | Unset = UNSET
    premium_end_date: datetime.datetime | None | Unset = UNSET
    premium_day_of_month: int | None | Unset = UNSET
    premium_month: int | None | Unset = UNSET
    premium_spacing: int | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str
        id = self.id

        vehicle: int | None | Unset
        if isinstance(self.vehicle, Unset):
            vehicle = UNSET
        else:
            vehicle = self.vehicle

        remainder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remainder, Unset):
            remainder = self.remainder.to_dict()

        remainder_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.remainder_date, Unset):
            remainder_date = self.remainder_date.to_dict()

        net_present_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.net_present_value, Unset):
            net_present_value = self.net_present_value.to_dict()

        net_present_value_date: dict[str, Any] | Unset = UNSET
        if not isinstance(self.net_present_value_date, Unset):
            net_present_value_date = self.net_present_value_date.to_dict()

        revocable: bool | None | Unset
        if isinstance(self.revocable, Unset):
            revocable = UNSET
        else:
            revocable = self.revocable

        realized = self.realized

        expected_maturity_year: int | None | Unset
        if isinstance(self.expected_maturity_year, Unset):
            expected_maturity_year = UNSET
        else:
            expected_maturity_year = self.expected_maturity_year

        status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        payout_percent: float | None | Unset
        if isinstance(self.payout_percent, Unset):
            payout_percent = UNSET
        else:
            payout_percent = self.payout_percent

        payout_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payout_amount, Unset):
            payout_amount = self.payout_amount.to_dict()

        flexible_deferred: bool | None | Unset
        if isinstance(self.flexible_deferred, Unset):
            flexible_deferred = UNSET
        else:
            flexible_deferred = self.flexible_deferred

        constituent_is_beneficiary = self.constituent_is_beneficiary

        term_type: int | None | Unset
        if isinstance(self.term_type, Unset):
            term_type = UNSET
        else:
            term_type = self.term_type

        term_end_date: None | str | Unset
        if isinstance(self.term_end_date, Unset):
            term_end_date = UNSET
        elif isinstance(self.term_end_date, datetime.datetime):
            term_end_date = self.term_end_date.isoformat()
        else:
            term_end_date = self.term_end_date

        trust_tax_id: None | str | Unset
        if isinstance(self.trust_tax_id, Unset):
            trust_tax_id = UNSET
        else:
            trust_tax_id = self.trust_tax_id

        discount_rate: float | None | Unset
        if isinstance(self.discount_rate, Unset):
            discount_rate = UNSET
        else:
            discount_rate = self.discount_rate

        payment_frequency: int | None | Unset
        if isinstance(self.payment_frequency, Unset):
            payment_frequency = UNSET
        else:
            payment_frequency = self.payment_frequency

        first_payment_date: None | str | Unset
        if isinstance(self.first_payment_date, Unset):
            first_payment_date = UNSET
        elif isinstance(self.first_payment_date, datetime.datetime):
            first_payment_date = self.first_payment_date.isoformat()
        else:
            first_payment_date = self.first_payment_date

        term_years: int | None | Unset
        if isinstance(self.term_years, Unset):
            term_years = UNSET
        else:
            term_years = self.term_years

        pooled_income_fund: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pooled_income_fund, Unset):
            pooled_income_fund = self.pooled_income_fund.to_dict()

        pooled_income_fund_units: int | None | Unset
        if isinstance(self.pooled_income_fund_units, Unset):
            pooled_income_fund_units = UNSET
        else:
            pooled_income_fund_units = self.pooled_income_fund_units

        pooled_income_fund_total_units: int | None | Unset
        if isinstance(self.pooled_income_fund_total_units, Unset):
            pooled_income_fund_total_units = UNSET
        else:
            pooled_income_fund_total_units = self.pooled_income_fund_total_units

        constituent_address_id: None | str | Unset
        if isinstance(self.constituent_address_id, Unset):
            constituent_address_id = UNSET
        else:
            constituent_address_id = self.constituent_address_id

        address_block: None | str | Unset
        if isinstance(self.address_block, Unset):
            address_block = UNSET
        else:
            address_block = self.address_block

        address_city: None | str | Unset
        if isinstance(self.address_city, Unset):
            address_city = UNSET
        else:
            address_city = self.address_city

        address_state: None | str | Unset
        if isinstance(self.address_state, Unset):
            address_state = UNSET
        else:
            address_state = self.address_state

        address_post_code: None | str | Unset
        if isinstance(self.address_post_code, Unset):
            address_post_code = UNSET
        else:
            address_post_code = self.address_post_code

        address_country: None | str | Unset
        if isinstance(self.address_country, Unset):
            address_country = UNSET
        else:
            address_country = self.address_country

        constituent_is_policy_owner = self.constituent_is_policy_owner

        constituent_pays_premium = self.constituent_pays_premium

        premium_is_fully_paid = self.premium_is_fully_paid

        insurance_carrier: None | str | Unset
        if isinstance(self.insurance_carrier, Unset):
            insurance_carrier = UNSET
        else:
            insurance_carrier = self.insurance_carrier

        policy_number: None | str | Unset
        if isinstance(self.policy_number, Unset):
            policy_number = UNSET
        else:
            policy_number = self.policy_number

        policy_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_type, Unset):
            policy_type = self.policy_type.to_dict()

        policy_face_amount: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_face_amount, Unset):
            policy_face_amount = self.policy_face_amount.to_dict()

        premium_frequency: str | Unset = UNSET
        if not isinstance(self.premium_frequency, Unset):
            premium_frequency = self.premium_frequency.value

        premium_start_date: None | str | Unset
        if isinstance(self.premium_start_date, Unset):
            premium_start_date = UNSET
        elif isinstance(self.premium_start_date, datetime.datetime):
            premium_start_date = self.premium_start_date.isoformat()
        else:
            premium_start_date = self.premium_start_date

        premium_end_date: None | str | Unset
        if isinstance(self.premium_end_date, Unset):
            premium_end_date = UNSET
        elif isinstance(self.premium_end_date, datetime.datetime):
            premium_end_date = self.premium_end_date.isoformat()
        else:
            premium_end_date = self.premium_end_date

        premium_day_of_month: int | None | Unset
        if isinstance(self.premium_day_of_month, Unset):
            premium_day_of_month = UNSET
        else:
            premium_day_of_month = self.premium_day_of_month

        premium_month: int | None | Unset
        if isinstance(self.premium_month, Unset):
            premium_month = UNSET
        else:
            premium_month = self.premium_month

        premium_spacing: int | None | Unset
        if isinstance(self.premium_spacing, Unset):
            premium_spacing = UNSET
        else:
            premium_spacing = self.premium_spacing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
            }
        )
        if vehicle is not UNSET:
            field_dict["vehicle"] = vehicle
        if remainder is not UNSET:
            field_dict["remainder"] = remainder
        if remainder_date is not UNSET:
            field_dict["remainder_date"] = remainder_date
        if net_present_value is not UNSET:
            field_dict["net_present_value"] = net_present_value
        if net_present_value_date is not UNSET:
            field_dict["net_present_value_date"] = net_present_value_date
        if revocable is not UNSET:
            field_dict["revocable"] = revocable
        if realized is not UNSET:
            field_dict["realized"] = realized
        if expected_maturity_year is not UNSET:
            field_dict["expected_maturity_year"] = expected_maturity_year
        if status is not UNSET:
            field_dict["status"] = status
        if payout_percent is not UNSET:
            field_dict["payout_percent"] = payout_percent
        if payout_amount is not UNSET:
            field_dict["payout_amount"] = payout_amount
        if flexible_deferred is not UNSET:
            field_dict["flexible_deferred"] = flexible_deferred
        if constituent_is_beneficiary is not UNSET:
            field_dict["constituent_is_beneficiary"] = constituent_is_beneficiary
        if term_type is not UNSET:
            field_dict["term_type"] = term_type
        if term_end_date is not UNSET:
            field_dict["term_end_date"] = term_end_date
        if trust_tax_id is not UNSET:
            field_dict["trust_tax_id"] = trust_tax_id
        if discount_rate is not UNSET:
            field_dict["discount_rate"] = discount_rate
        if payment_frequency is not UNSET:
            field_dict["payment_frequency"] = payment_frequency
        if first_payment_date is not UNSET:
            field_dict["first_payment_date"] = first_payment_date
        if term_years is not UNSET:
            field_dict["term_years"] = term_years
        if pooled_income_fund is not UNSET:
            field_dict["pooled_income_fund"] = pooled_income_fund
        if pooled_income_fund_units is not UNSET:
            field_dict["pooled_income_fund_units"] = pooled_income_fund_units
        if pooled_income_fund_total_units is not UNSET:
            field_dict["pooled_income_fund_total_units"] = (
                pooled_income_fund_total_units
            )
        if constituent_address_id is not UNSET:
            field_dict["constituent_address_id"] = constituent_address_id
        if address_block is not UNSET:
            field_dict["address_block"] = address_block
        if address_city is not UNSET:
            field_dict["address_city"] = address_city
        if address_state is not UNSET:
            field_dict["address_state"] = address_state
        if address_post_code is not UNSET:
            field_dict["address_post_code"] = address_post_code
        if address_country is not UNSET:
            field_dict["address_country"] = address_country
        if constituent_is_policy_owner is not UNSET:
            field_dict["constituent_is_policy_owner"] = constituent_is_policy_owner
        if constituent_pays_premium is not UNSET:
            field_dict["constituent_pays_premium"] = constituent_pays_premium
        if premium_is_fully_paid is not UNSET:
            field_dict["premium_is_fully_paid"] = premium_is_fully_paid
        if insurance_carrier is not UNSET:
            field_dict["insurance_carrier"] = insurance_carrier
        if policy_number is not UNSET:
            field_dict["policy_number"] = policy_number
        if policy_type is not UNSET:
            field_dict["policy_type"] = policy_type
        if policy_face_amount is not UNSET:
            field_dict["policy_face_amount"] = policy_face_amount
        if premium_frequency is not UNSET:
            field_dict["premium_frequency"] = premium_frequency
        if premium_start_date is not UNSET:
            field_dict["premium_start_date"] = premium_start_date
        if premium_end_date is not UNSET:
            field_dict["premium_end_date"] = premium_end_date
        if premium_day_of_month is not UNSET:
            field_dict["premium_day_of_month"] = premium_day_of_month
        if premium_month is not UNSET:
            field_dict["premium_month"] = premium_month
        if premium_spacing is not UNSET:
            field_dict["premium_spacing"] = premium_spacing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry
        from ..models.currency import Currency
        from ..models.fuzzy_date import FuzzyDate

        d = dict(src_dict)

        def _parse_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        id = _parse_id(d.pop("id"))

        def _parse_vehicle(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        vehicle = _parse_vehicle(d.pop("vehicle", UNSET))

        _remainder = d.pop("remainder", UNSET)
        remainder: Currency | Unset
        if isinstance(_remainder, Unset):
            remainder = UNSET
        else:
            remainder = Currency.from_dict(_remainder)

        _remainder_date = d.pop("remainder_date", UNSET)
        remainder_date: FuzzyDate | Unset
        if isinstance(_remainder_date, Unset):
            remainder_date = UNSET
        else:
            remainder_date = FuzzyDate.from_dict(_remainder_date)

        _net_present_value = d.pop("net_present_value", UNSET)
        net_present_value: Currency | Unset
        if isinstance(_net_present_value, Unset):
            net_present_value = UNSET
        else:
            net_present_value = Currency.from_dict(_net_present_value)

        _net_present_value_date = d.pop("net_present_value_date", UNSET)
        net_present_value_date: FuzzyDate | Unset
        if isinstance(_net_present_value_date, Unset):
            net_present_value_date = UNSET
        else:
            net_present_value_date = FuzzyDate.from_dict(_net_present_value_date)

        def _parse_revocable(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        revocable = _parse_revocable(d.pop("revocable", UNSET))

        realized = d.pop("realized", UNSET)

        def _parse_expected_maturity_year(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_maturity_year = _parse_expected_maturity_year(
            d.pop("expected_maturity_year", UNSET)
        )

        _status = d.pop("status", UNSET)
        status: CodeTableEntry | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CodeTableEntry.from_dict(_status)

        def _parse_payout_percent(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        payout_percent = _parse_payout_percent(d.pop("payout_percent", UNSET))

        _payout_amount = d.pop("payout_amount", UNSET)
        payout_amount: Currency | Unset
        if isinstance(_payout_amount, Unset):
            payout_amount = UNSET
        else:
            payout_amount = Currency.from_dict(_payout_amount)

        def _parse_flexible_deferred(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        flexible_deferred = _parse_flexible_deferred(d.pop("flexible_deferred", UNSET))

        constituent_is_beneficiary = d.pop("constituent_is_beneficiary", UNSET)

        def _parse_term_type(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        term_type = _parse_term_type(d.pop("term_type", UNSET))

        def _parse_term_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                term_end_date_type_0 = isoparse(data)

                return term_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        term_end_date = _parse_term_end_date(d.pop("term_end_date", UNSET))

        def _parse_trust_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trust_tax_id = _parse_trust_tax_id(d.pop("trust_tax_id", UNSET))

        def _parse_discount_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        discount_rate = _parse_discount_rate(d.pop("discount_rate", UNSET))

        def _parse_payment_frequency(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        payment_frequency = _parse_payment_frequency(d.pop("payment_frequency", UNSET))

        def _parse_first_payment_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_payment_date_type_0 = isoparse(data)

                return first_payment_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        first_payment_date = _parse_first_payment_date(
            d.pop("first_payment_date", UNSET)
        )

        def _parse_term_years(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        term_years = _parse_term_years(d.pop("term_years", UNSET))

        _pooled_income_fund = d.pop("pooled_income_fund", UNSET)
        pooled_income_fund: CodeTableEntry | Unset
        if isinstance(_pooled_income_fund, Unset):
            pooled_income_fund = UNSET
        else:
            pooled_income_fund = CodeTableEntry.from_dict(_pooled_income_fund)

        def _parse_pooled_income_fund_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pooled_income_fund_units = _parse_pooled_income_fund_units(
            d.pop("pooled_income_fund_units", UNSET)
        )

        def _parse_pooled_income_fund_total_units(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        pooled_income_fund_total_units = _parse_pooled_income_fund_total_units(
            d.pop("pooled_income_fund_total_units", UNSET)
        )

        def _parse_constituent_address_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_address_id = _parse_constituent_address_id(
            d.pop("constituent_address_id", UNSET)
        )

        def _parse_address_block(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_block = _parse_address_block(d.pop("address_block", UNSET))

        def _parse_address_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_city = _parse_address_city(d.pop("address_city", UNSET))

        def _parse_address_state(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_state = _parse_address_state(d.pop("address_state", UNSET))

        def _parse_address_post_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_post_code = _parse_address_post_code(d.pop("address_post_code", UNSET))

        def _parse_address_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        address_country = _parse_address_country(d.pop("address_country", UNSET))

        constituent_is_policy_owner = d.pop("constituent_is_policy_owner", UNSET)

        constituent_pays_premium = d.pop("constituent_pays_premium", UNSET)

        premium_is_fully_paid = d.pop("premium_is_fully_paid", UNSET)

        def _parse_insurance_carrier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        insurance_carrier = _parse_insurance_carrier(d.pop("insurance_carrier", UNSET))

        def _parse_policy_number(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        policy_number = _parse_policy_number(d.pop("policy_number", UNSET))

        _policy_type = d.pop("policy_type", UNSET)
        policy_type: CodeTableEntry | Unset
        if isinstance(_policy_type, Unset):
            policy_type = UNSET
        else:
            policy_type = CodeTableEntry.from_dict(_policy_type)

        _policy_face_amount = d.pop("policy_face_amount", UNSET)
        policy_face_amount: Currency | Unset
        if isinstance(_policy_face_amount, Unset):
            policy_face_amount = UNSET
        else:
            policy_face_amount = Currency.from_dict(_policy_face_amount)

        _premium_frequency = d.pop("premium_frequency", UNSET)
        premium_frequency: PremiumFrequency | Unset
        if isinstance(_premium_frequency, Unset):
            premium_frequency = UNSET
        else:
            premium_frequency = PremiumFrequency(_premium_frequency)

        def _parse_premium_start_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                premium_start_date_type_0 = isoparse(data)

                return premium_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        premium_start_date = _parse_premium_start_date(
            d.pop("premium_start_date", UNSET)
        )

        def _parse_premium_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                premium_end_date_type_0 = isoparse(data)

                return premium_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        premium_end_date = _parse_premium_end_date(d.pop("premium_end_date", UNSET))

        def _parse_premium_day_of_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premium_day_of_month = _parse_premium_day_of_month(
            d.pop("premium_day_of_month", UNSET)
        )

        def _parse_premium_month(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premium_month = _parse_premium_month(d.pop("premium_month", UNSET))

        def _parse_premium_spacing(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        premium_spacing = _parse_premium_spacing(d.pop("premium_spacing", UNSET))

        planned_gift_read = cls(
            id=id,
            vehicle=vehicle,
            remainder=remainder,
            remainder_date=remainder_date,
            net_present_value=net_present_value,
            net_present_value_date=net_present_value_date,
            revocable=revocable,
            realized=realized,
            expected_maturity_year=expected_maturity_year,
            status=status,
            payout_percent=payout_percent,
            payout_amount=payout_amount,
            flexible_deferred=flexible_deferred,
            constituent_is_beneficiary=constituent_is_beneficiary,
            term_type=term_type,
            term_end_date=term_end_date,
            trust_tax_id=trust_tax_id,
            discount_rate=discount_rate,
            payment_frequency=payment_frequency,
            first_payment_date=first_payment_date,
            term_years=term_years,
            pooled_income_fund=pooled_income_fund,
            pooled_income_fund_units=pooled_income_fund_units,
            pooled_income_fund_total_units=pooled_income_fund_total_units,
            constituent_address_id=constituent_address_id,
            address_block=address_block,
            address_city=address_city,
            address_state=address_state,
            address_post_code=address_post_code,
            address_country=address_country,
            constituent_is_policy_owner=constituent_is_policy_owner,
            constituent_pays_premium=constituent_pays_premium,
            premium_is_fully_paid=premium_is_fully_paid,
            insurance_carrier=insurance_carrier,
            policy_number=policy_number,
            policy_type=policy_type,
            policy_face_amount=policy_face_amount,
            premium_frequency=premium_frequency,
            premium_start_date=premium_start_date,
            premium_end_date=premium_end_date,
            premium_day_of_month=premium_day_of_month,
            premium_month=premium_month,
            premium_spacing=premium_spacing,
        )

        return planned_gift_read
