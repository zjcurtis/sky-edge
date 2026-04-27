from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_batch_gift_add import GiftBatchGiftAdd


T = TypeVar("T", bound="GiftsAdd")


@_attrs_define
class GiftsAdd:
    """
    Example:
        {'gifts': [{'amount': {'value': 100}, 'constituent_id': '280', 'date': '2017-10-03T00:00:00.0000000+00:00',
            'fundraisers': [{'amount': {'value': 100}, 'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100},
            'appeal_id': '15', 'campaign_id': '1', 'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False,
            'lookup_id': '2225', 'payments': [{'payment_method': 'Cash'}], 'post_date': '2017-10-03T00:00:00.0000000+00:00',
            'post_status': 'NotPosted', 'reference': 'newly added gift', 'soft_credits': [{'amount': {'value': 100},
            'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation'}, {'amount': {'value': 100},
            'constituent_id': '290', 'date': '2017-10-03T00:00:00.0000000+00:00', 'fundraisers': [{'amount': {'value': 100},
            'constituent_id': '252'}], 'gift_splits': [{'amount': {'value': 100}, 'appeal_id': '15', 'campaign_id': '1',
            'fund_id': '41'}], 'gift_status': 'Active', 'is_anonymous': False, 'lookup_id': '2225', 'origin': '{"name":
            "Gift origin name"}', 'payments': [{'payment_method': 'Cash'}], 'post_date':
            '2017-10-03T00:00:00.0000000+00:00', 'post_status': 'NotPosted', 'reference': 'newly added gift',
            'soft_credits': [{'amount': {'value': 100}, 'constituent_id': '187'}], 'subtype': 'Annuity', 'type': 'Donation',
            'tributes': [{'id': '12'}, {'id': '15', 'tribute_acknowledgees': [{'id': '33'}, {'id': '21'}]}]}]}

    Attributes:
        gifts (list[GiftBatchGiftAdd] | Unset): The set of gifts.
    """

    gifts: list[GiftBatchGiftAdd] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        gifts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.gifts, Unset):
            gifts = []
            for gifts_item_data in self.gifts:
                gifts_item = gifts_item_data.to_dict()
                gifts.append(gifts_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gifts is not UNSET:
            field_dict["gifts"] = gifts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_batch_gift_add import GiftBatchGiftAdd

        d = dict(src_dict)
        _gifts = d.pop("gifts", UNSET)
        gifts: list[GiftBatchGiftAdd] | Unset = UNSET
        if _gifts is not UNSET:
            gifts = []
            for gifts_item_data in _gifts:
                gifts_item = GiftBatchGiftAdd.from_dict(gifts_item_data)

                gifts.append(gifts_item)

        gifts_add = cls(
            gifts=gifts,
        )

        gifts_add.additional_properties = d
        return gifts_add

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
