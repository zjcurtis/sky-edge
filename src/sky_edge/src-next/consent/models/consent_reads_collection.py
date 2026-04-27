from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.consent_read import ConsentRead


T = TypeVar("T", bound="ConsentReadsCollection")


@_attrs_define
class ConsentReadsCollection:
    """Consent reads collection

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection. Default: 0.
        limit (int): The limit representing the maximum number of items to retrieve or display. Default: 500.
        consents (list[ConsentRead] | None | Unset): The list of consents.
        count (int | Unset): The total number of items in the collection.
        continuation_token (None | str | Unset): The continuation token used for pagination to retrieve the next set of
            results.
    """

    offset: int = 0
    limit: int = 500
    consents: list[ConsentRead] | None | Unset = UNSET
    count: int | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        consents: list[dict[str, Any]] | None | Unset
        if isinstance(self.consents, Unset):
            consents = UNSET
        elif isinstance(self.consents, list):
            consents = []
            for consents_type_0_item_data in self.consents:
                consents_type_0_item = consents_type_0_item_data.to_dict()
                consents.append(consents_type_0_item)

        else:
            consents = self.consents

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
        if consents is not UNSET:
            field_dict["consents"] = consents
        if count is not UNSET:
            field_dict["count"] = count
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.consent_read import ConsentRead

        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_consents(data: object) -> list[ConsentRead] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                consents_type_0 = []
                _consents_type_0 = data
                for consents_type_0_item_data in _consents_type_0:
                    consents_type_0_item = ConsentRead.from_dict(consents_type_0_item_data)

                    consents_type_0.append(consents_type_0_item)

                return consents_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConsentRead] | None | Unset, data)

        consents = _parse_consents(d.pop("consents", UNSET))

        count = d.pop("count", UNSET)

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token", UNSET))

        consent_reads_collection = cls(
            offset=offset,
            limit=limit,
            consents=consents,
            count=count,
            continuation_token=continuation_token,
        )

        return consent_reads_collection
