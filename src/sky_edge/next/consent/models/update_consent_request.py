from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="UpdateConsentRequest")


@_attrs_define
class UpdateConsentRequest:
    """Defines model to represent update consent request.

    Attributes:
        consent_statement (None | str | Unset): The consent statement.
        privacy_notice (None | str | Unset): The privacy policy.
        source (None | str | Unset): The source of the consent.
    """

    consent_statement: None | str | Unset = UNSET
    privacy_notice: None | str | Unset = UNSET
    source: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consent_statement: None | str | Unset
        if isinstance(self.consent_statement, Unset):
            consent_statement = UNSET
        else:
            consent_statement = self.consent_statement

        privacy_notice: None | str | Unset
        if isinstance(self.privacy_notice, Unset):
            privacy_notice = UNSET
        else:
            privacy_notice = self.privacy_notice

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if consent_statement is not UNSET:
            field_dict["consent_statement"] = consent_statement
        if privacy_notice is not UNSET:
            field_dict["privacy_notice"] = privacy_notice
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_consent_statement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consent_statement = _parse_consent_statement(d.pop("consent_statement", UNSET))

        def _parse_privacy_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_notice = _parse_privacy_notice(d.pop("privacy_notice", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        update_consent_request = cls(
            consent_statement=consent_statement,
            privacy_notice=privacy_notice,
            source=source,
        )

        return update_consent_request
