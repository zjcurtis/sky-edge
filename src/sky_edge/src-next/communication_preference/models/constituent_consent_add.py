from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.constituent_consent_add_constituent_consent_response import (
    ConstituentConsentAddConstituentConsentResponse,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConstituentConsentAdd")


@_attrs_define
class ConstituentConsentAdd:
    """Represents the consent entity to add to the specified constituent.

    Attributes:
        constituent_id (str): The immutable system record ID of the constituent associated with the consent record.
        channel (str): The channel that the consent response applies to. Available values can be obtained from the <a
            href="https://developer.sky.blackbaud.com/docs/services/communication-
            preference/operations/ListConsentChannels">Consent Channels List</a>.
        consent_date (datetime.datetime): The date the consent response was received.
        constituent_consent_response (ConstituentConsentAddConstituentConsentResponse): How the constituent responded to
            consent for the specified channel/category. Available values are <i>OptIn</i>, <i>OptOut</i>, and
            <i>NoResponse</i>.
        category (None | str | Unset): The category that the consent response applies to. Available values can be
            obtained from the <a href="https://developer.sky.blackbaud.com/docs/services/communication-
            preference/operations/ListConsentCategories">Consent Categories List</a>.
        source (None | str | Unset): The source of the consent response from the constituent. Available values can be
            obtained from the <a href="https://developer.sky.blackbaud.com/docs/services/communication-
            preference/operations/ListConsentSources">Consent Sources List</a>.
        privacy_notice (None | str | Unset): The privacy notice provided to the constituent.
        consent_statement (None | str | Unset): The statement the constituent responded to when providing consent.
        user_name (None | str | Unset): The user name associated with the consent. If not supplied, will have a default
            set based on the user's account.
    """

    constituent_id: str
    channel: str
    consent_date: datetime.datetime
    constituent_consent_response: ConstituentConsentAddConstituentConsentResponse
    category: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    privacy_notice: None | str | Unset = UNSET
    consent_statement: None | str | Unset = UNSET
    user_name: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        channel = self.channel

        consent_date = self.consent_date.isoformat()

        constituent_consent_response = self.constituent_consent_response.value

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

        privacy_notice: None | str | Unset
        if isinstance(self.privacy_notice, Unset):
            privacy_notice = UNSET
        else:
            privacy_notice = self.privacy_notice

        consent_statement: None | str | Unset
        if isinstance(self.consent_statement, Unset):
            consent_statement = UNSET
        else:
            consent_statement = self.consent_statement

        user_name: None | str | Unset
        if isinstance(self.user_name, Unset):
            user_name = UNSET
        else:
            user_name = self.user_name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "constituent_id": constituent_id,
                "channel": channel,
                "consent_date": consent_date,
                "constituent_consent_response": constituent_consent_response,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if source is not UNSET:
            field_dict["source"] = source
        if privacy_notice is not UNSET:
            field_dict["privacy_notice"] = privacy_notice
        if consent_statement is not UNSET:
            field_dict["consent_statement"] = consent_statement
        if user_name is not UNSET:
            field_dict["user_name"] = user_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        channel = d.pop("channel")

        consent_date = isoparse(d.pop("consent_date"))

        constituent_consent_response = ConstituentConsentAddConstituentConsentResponse(
            d.pop("constituent_consent_response")
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

        def _parse_privacy_notice(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        privacy_notice = _parse_privacy_notice(d.pop("privacy_notice", UNSET))

        def _parse_consent_statement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        consent_statement = _parse_consent_statement(d.pop("consent_statement", UNSET))

        def _parse_user_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        user_name = _parse_user_name(d.pop("user_name", UNSET))

        constituent_consent_add = cls(
            constituent_id=constituent_id,
            channel=channel,
            consent_date=consent_date,
            constituent_consent_response=constituent_consent_response,
            category=category,
            source=source,
            privacy_notice=privacy_notice,
            consent_statement=consent_statement,
            user_name=user_name,
        )

        return constituent_consent_add
