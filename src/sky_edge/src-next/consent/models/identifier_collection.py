from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentifierCollection")


@_attrs_define
class IdentifierCollection:
    """Collection of identifiers resulting from a bulk add request

    Attributes:
        offset (int): The offset value used for pagination or positioning within a collection. Default: 0.
        limit (int): The limit representing the maximum number of items to retrieve or display. Default: 500.
        identifiers (list[str] | None | Unset): The list of consent identifiers.
        count (int | Unset): The total number of items in the collection.
        continuation_token (None | str | Unset): The continuation token used for pagination to retrieve the next set of
            results.
    """

    offset: int = 0
    limit: int = 500
    identifiers: list[str] | None | Unset = UNSET
    count: int | Unset = UNSET
    continuation_token: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        offset = self.offset

        limit = self.limit

        identifiers: list[str] | None | Unset
        if isinstance(self.identifiers, Unset):
            identifiers = UNSET
        elif isinstance(self.identifiers, list):
            identifiers = self.identifiers

        else:
            identifiers = self.identifiers

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
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if count is not UNSET:
            field_dict["count"] = count
        if continuation_token is not UNSET:
            field_dict["continuation_token"] = continuation_token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        offset = d.pop("offset")

        limit = d.pop("limit")

        def _parse_identifiers(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                identifiers_type_0 = cast(list[str], data)

                return identifiers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        identifiers = _parse_identifiers(d.pop("identifiers", UNSET))

        count = d.pop("count", UNSET)

        def _parse_continuation_token(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        continuation_token = _parse_continuation_token(d.pop("continuation_token", UNSET))

        identifier_collection = cls(
            offset=offset,
            limit=limit,
            identifiers=identifiers,
            count=count,
            continuation_token=continuation_token,
        )

        return identifier_collection
