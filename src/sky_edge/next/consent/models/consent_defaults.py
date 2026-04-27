from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ConsentDefaults")


@_attrs_define
class ConsentDefaults:
    """Defines model to represent consent defaults.

    Attributes:
        consent_statement (None | str | Unset): Consent statement for consent configuration.
        privacy_policy (None | str | Unset): Privacy policy for consent configuration.
    """

    consent_statement: None | str | Unset = UNSET
    privacy_policy: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        consent_statement: None | str | Unset
        if isinstance(self.consent_statement, Unset):
            consent_statement = UNSET
        else:
            consent_statement = self.consent_statement

        privacy_policy: None | str | Unset
        if isinstance(self.privacy_policy, Unset):
            privacy_policy = UNSET
        else:
            privacy_policy = self.privacy_policy

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if consent_statement is not UNSET:
            field_dict["consent_statement"] = consent_statement
        if privacy_policy is not UNSET:
            field_dict["privacy_policy"] = privacy_policy

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

        def _parse_privacy_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_policy = _parse_privacy_policy(d.pop("privacy_policy", UNSET))

        consent_defaults = cls(
            consent_statement=consent_statement,
            privacy_policy=privacy_policy,
        )

        return consent_defaults
