from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constituent_consent_read import ConstituentConsentRead


T = TypeVar("T", bound="ConstituentConsentReadCollection")


@_attrs_define
class ConstituentConsentReadCollection:
    """Represents a collection of paginated constituent consents

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection. Default: 0.
        limit (int): The limit representing the maximum number of items to retrieve or display. Default: 500.
        constituent_consents (list[ConstituentConsentRead] | None | Unset): The list of constituent consents.
        count (int | Unset): The total number of items in the collection.
        continuation_token (None | str | Unset): The continuation token used for pagination to retrieve the next set of
            results.
    """

    offset: int = 0
    limit: int = 500
    constituent_consents: list[ConstituentConsentRead] | None | Unset = UNSET
    count: int | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        constituent_consents: list[dict[str, Any]] | None | Unset
        if isinstance(self.constituent_consents, Unset):
            constituent_consents = UNSET
        elif isinstance(self.constituent_consents, list):
            constituent_consents = []
            for constituent_consents_type_0_item_data in self.constituent_consents:
                constituent_consents_type_0_item = (
                    constituent_consents_type_0_item_data.to_dict()
                )
                constituent_consents.append(constituent_consents_type_0_item)

        else:
            constituent_consents = self.constituent_consents

        count = self.count

        continuation_token: None | str | Unset
        if isinstance(self.continuation_token, Unset):
            continuation_token = UNSET
        else:
            continuation_token = self.continuation_token

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "offset": offset,
                "limit": limit,
            }
        )
        if constituent_consents is not UNSET:
            field_dict["constituent_consents"] = constituent_consents
        if count is not UNSET:
            field_dict["count"] = count
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constituent_consent_read import ConstituentConsentRead

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_constituent_consents(
            data: object,
        ) -> list[ConstituentConsentRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                constituent_consents_type_0 = []
                _constituent_consents_type_0 = data
                for (
                    constituent_consents_type_0_item_data
                ) in _constituent_consents_type_0:
                    constituent_consents_type_0_item = ConstituentConsentRead.from_dict(
                        constituent_consents_type_0_item_data
                    )

                    constituent_consents_type_0.append(constituent_consents_type_0_item)

                return constituent_consents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConstituentConsentRead] | None | Unset, data)

        constituent_consents = _parse_constituent_consents(
            d.pop("constituent_consents", UNSET)
        )

        count = d.pop("count", UNSET)

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(
            d.pop("continuation_token", UNSET)
        )

        constituent_consent_read_collection = cls(
            offset=offset,
            limit=limit,
            constituent_consents=constituent_consents,
            count=count,
            continuation_token=continuation_token,
        )

        return constituent_consent_read_collection
