from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.renewal_notice_information import RenewalNoticeInformation


T = TypeVar("T", bound="RenewalNoticeInformationCollection")


@_attrs_define
class RenewalNoticeInformationCollection:
    """Defines a collection of renewal notice information.

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection.
        limit (int): The limit representing the maximum number of items to retrieve or display.
        renewal_notices (list[RenewalNoticeInformation] | None | Unset): The collection of renewal notices.
        count (int | Unset): The total count of items.
    """

    offset: int
    limit: int
    renewal_notices: list[RenewalNoticeInformation] | None | Unset = UNSET
    count: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        renewal_notices: list[dict[str, Any]] | None | Unset
        if isinstance(self.renewal_notices, Unset):
            renewal_notices = UNSET
        elif isinstance(self.renewal_notices, list):
            renewal_notices = []
            for renewal_notices_type_0_item_data in self.renewal_notices:
                renewal_notices_type_0_item = renewal_notices_type_0_item_data.to_dict()
                renewal_notices.append(renewal_notices_type_0_item)

        else:
            renewal_notices = self.renewal_notices

        count = self.count

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if renewal_notices is not UNSET:
            field_dict["renewal_notices"] = renewal_notices
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.renewal_notice_information import RenewalNoticeInformation

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_renewal_notices(data: object) -> list[RenewalNoticeInformation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                renewal_notices_type_0 = []
                _renewal_notices_type_0 = data
                for renewal_notices_type_0_item_data in _renewal_notices_type_0:
                    renewal_notices_type_0_item = RenewalNoticeInformation.from_dict(renewal_notices_type_0_item_data)

                    renewal_notices_type_0.append(renewal_notices_type_0_item)

                return renewal_notices_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RenewalNoticeInformation] | None | Unset, data)

        renewal_notices = _parse_renewal_notices(d.pop("renewal_notices", UNSET))

        count = d.pop("count", UNSET)

        renewal_notice_information_collection = cls(
            offset=offset,
            limit=limit,
            renewal_notices=renewal_notices,
            count=count,
        )

        return renewal_notice_information_collection
