from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.matching_gift_credit_option import MatchingGiftCreditOption
from ..models.soft_credit_option import SoftCreditOption
from ..models.soft_credit_sub_option import SoftCreditSubOption
from ..types import UNSET, Unset

T = TypeVar("T", bound="GiftProcessingOptions")


@_attrs_define
class GiftProcessingOptions:
    """Query options for gift processing specific to RE

    Attributes:
        soft_credit_option (SoftCreditOption | Unset): Soft Credit
            Options<p>Members:</p><ul><li><i>Donor</i></li><li><i>Recipients</i></li><li><i>Both</i></li></ul>
        soft_credit_sub_option (SoftCreditSubOption | Unset): Soft credit suboptions for the distributions<p>Members:</p
            ><ul><li><i>UseAmountInGrid</i></li><li><i>FullAmountToAll</i></li><li><i>SplitEvenly</i></li></ul>
        matching_gift_credit_option (MatchingGiftCreditOption | Unset): Match Credit
            Options<p>Members:</p><ul><li><i>Donor</i></li><li><i>MatchingGiftCompany</i></li><li><i>Both</i></li></ul>
        use_gross_amount_for_covenants (bool | Unset): Gift processing gross amount option for UK Gift Aid (Net or Gross
            amount)
    """

    soft_credit_option: SoftCreditOption | Unset = UNSET
    soft_credit_sub_option: SoftCreditSubOption | Unset = UNSET
    matching_gift_credit_option: MatchingGiftCreditOption | Unset = UNSET
    use_gross_amount_for_covenants: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        soft_credit_option: str | Unset = UNSET
        if not isinstance(self.soft_credit_option, Unset):
            soft_credit_option = self.soft_credit_option.value

        soft_credit_sub_option: str | Unset = UNSET
        if not isinstance(self.soft_credit_sub_option, Unset):
            soft_credit_sub_option = self.soft_credit_sub_option.value

        matching_gift_credit_option: str | Unset = UNSET
        if not isinstance(self.matching_gift_credit_option, Unset):
            matching_gift_credit_option = self.matching_gift_credit_option.value

        use_gross_amount_for_covenants = self.use_gross_amount_for_covenants

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if soft_credit_option is not UNSET:
            field_dict["soft_credit_option"] = soft_credit_option
        if soft_credit_sub_option is not UNSET:
            field_dict["soft_credit_sub_option"] = soft_credit_sub_option
        if matching_gift_credit_option is not UNSET:
            field_dict["matching_gift_credit_option"] = matching_gift_credit_option
        if use_gross_amount_for_covenants is not UNSET:
            field_dict["use_gross_amount_for_covenants"] = use_gross_amount_for_covenants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _soft_credit_option = d.pop("soft_credit_option", UNSET)
        soft_credit_option: SoftCreditOption | Unset
        if isinstance(_soft_credit_option, Unset):
            soft_credit_option = UNSET
        else:
            soft_credit_option = SoftCreditOption(_soft_credit_option)

        _soft_credit_sub_option = d.pop("soft_credit_sub_option", UNSET)
        soft_credit_sub_option: SoftCreditSubOption | Unset
        if isinstance(_soft_credit_sub_option, Unset):
            soft_credit_sub_option = UNSET
        else:
            soft_credit_sub_option = SoftCreditSubOption(_soft_credit_sub_option)

        _matching_gift_credit_option = d.pop("matching_gift_credit_option", UNSET)
        matching_gift_credit_option: MatchingGiftCreditOption | Unset
        if isinstance(_matching_gift_credit_option, Unset):
            matching_gift_credit_option = UNSET
        else:
            matching_gift_credit_option = MatchingGiftCreditOption(_matching_gift_credit_option)

        use_gross_amount_for_covenants = d.pop("use_gross_amount_for_covenants", UNSET)

        gift_processing_options = cls(
            soft_credit_option=soft_credit_option,
            soft_credit_sub_option=soft_credit_sub_option,
            matching_gift_credit_option=matching_gift_credit_option,
            use_gross_amount_for_covenants=use_gross_amount_for_covenants,
        )

        return gift_processing_options
