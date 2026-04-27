from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.create_consent_request_channel import CreateConsentRequestChannel
from ..models.create_consent_request_consent_response import (
    CreateConsentRequestConsentResponse,
)

T = TypeVar("T", bound="CreateConsentRequest")


@_attrs_define
class CreateConsentRequest:
    """Model used by SkyApi to create consent records for a single constituent

    Attributes:
        channel (CreateConsentRequestChannel): The name of the channel.<p>Members:</p><ul><li><i>Email</i> -
            Email</li><li><i>Mail</i> - Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i>
            - AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        consent_date (datetime.datetime): Date on which the consent response was provided.
        consent_response (CreateConsentRequestConsentResponse): The consent response provided by the
            constituent.<p>Members:</p><ul><li><i>OptIn</i> - Opt-in</li><li><i>OptOut</i> - Opt-
            out</li><li><i>NoResponse</i> - No response</li></ul>
        category (None | str | Unset): The name of the category.
        source (None | str | Unset): The name of the source.
        privacy_policy (None | str | Unset): Privacy policy for consent.
        consent_statement (None | str | Unset): Consent statement for consent.
    """

    channel: CreateConsentRequestChannel
    consent_date: datetime.datetime
    consent_response: CreateConsentRequestConsentResponse
    category: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    privacy_policy: None | str | Unset = UNSET
    consent_statement: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

        consent_date = self.consent_date.isoformat()

        consent_response = self.consent_response.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        source: None | str | Unset
        if isinstance(self.source, Unset):
            source = UNSET
        else:
            source = self.source

        privacy_policy: None | str | Unset
        if isinstance(self.privacy_policy, Unset):
            privacy_policy = UNSET
        else:
            privacy_policy = self.privacy_policy

        consent_statement: None | str | Unset
        if isinstance(self.consent_statement, Unset):
            consent_statement = UNSET
        else:
            consent_statement = self.consent_statement

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channel": channel,
                "consent_date": consent_date,
                "consent_response": consent_response,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if source is not UNSET:
            field_dict["source"] = source
        if privacy_policy is not UNSET:
            field_dict["privacy_policy"] = privacy_policy
        if consent_statement is not UNSET:
            field_dict["consent_statement"] = consent_statement

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        channel = CreateConsentRequestChannel(d.pop("channel"))

        consent_date = isoparse(d.pop("consent_date"))

        consent_response = CreateConsentRequestConsentResponse(
            d.pop("consent_response")
        )

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source = _parse_source(d.pop("source", UNSET))

        def _parse_privacy_policy(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_policy = _parse_privacy_policy(d.pop("privacy_policy", UNSET))

        def _parse_consent_statement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consent_statement = _parse_consent_statement(d.pop("consent_statement", UNSET))

        create_consent_request = cls(
            channel=channel,
            consent_date=consent_date,
            consent_response=consent_response,
            category=category,
            source=source,
            privacy_policy=privacy_policy,
            consent_statement=consent_statement,
        )

        return create_consent_request
