from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

from ..models.constituent_consent_read_channel import ConstituentConsentReadChannel
from ..models.constituent_consent_read_response import ConstituentConsentReadResponse

T = TypeVar("T", bound="ConstituentConsentRead")


@_attrs_define
class ConstituentConsentRead:
    """Represents a consent record associated with a specific constituent.

    Attributes:
        constituent_id (None | str | Unset): The system record identifier of the constituent to whom this consent record
            applies.
        id (None | str | Unset): The immutable system record ID of the consent record.
        channel (ConstituentConsentReadChannel | Unset): The channel that the consent response applies
            to.<p>Members:</p><ul><li><i>Email</i> - Email</li><li><i>Mail</i> - Mail</li><li><i>SMS</i> -
            SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i> - AutoPhone</li><li><i>Social</i> - Social
            media</li><li><i>DataProcessing</i> - Data processing</li><li><i>Other</i> - Other</li></ul>
        inactive (bool | None | Unset): Flag indicating whether or not the consent channel is inactive.
        date (datetime.datetime | Unset): The date the consent response was received.
        response (ConstituentConsentReadResponse | Unset): How the constituent responded to consent for the specified
            channel/category.<p>Members:</p><ul><li><i>OptIn</i> - Opt-in</li><li><i>OptOut</i> - Opt-
            out</li><li><i>NoResponse</i> - No response</li></ul>
        category (None | str | Unset): The category that the consent response applies to.
        category_id (None | str | Unset): The category identifier.
        source (None | str | Unset): The source of the consent response from the constituent.
        privacy_notice (None | str | Unset): The privacy notice provided to the constituent.
        consent_statement (None | str | Unset): The statement the constituent responded to when providing consent.
        date_added (datetime.datetime | Unset): The UTC DateTime the consent response was added to the system.
    """

    constituent_id: None | str | Unset = UNSET
    id: None | str | Unset = UNSET
    channel: ConstituentConsentReadChannel | Unset = UNSET
    inactive: bool | None | Unset = UNSET
    date: datetime.datetime | Unset = UNSET
    response: ConstituentConsentReadResponse | Unset = UNSET
    category: None | str | Unset = UNSET
    category_id: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    privacy_notice: None | str | Unset = UNSET
    consent_statement: None | str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        constituent_id: None | str | Unset
        if isinstance(self.constituent_id, Unset):
            constituent_id = UNSET
        else:
            constituent_id = self.constituent_id

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        inactive: bool | None | Unset
        if isinstance(self.inactive, Unset):
            inactive = UNSET
        else:
            inactive = self.inactive

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        response: str | Unset = UNSET
        if not isinstance(self.response, Unset):
            response = self.response.value

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        category_id: None | str | Unset
        if isinstance(self.category_id, Unset):
            category_id = UNSET
        else:
            category_id = self.category_id

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

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if id is not UNSET:
            field_dict["id"] = id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if date is not UNSET:
            field_dict["date"] = date
        if response is not UNSET:
            field_dict["response"] = response
        if category is not UNSET:
            field_dict["category"] = category
        if category_id is not UNSET:
            field_dict["category_id"] = category_id
        if source is not UNSET:
            field_dict["source"] = source
        if privacy_notice is not UNSET:
            field_dict["privacy_notice"] = privacy_notice
        if consent_statement is not UNSET:
            field_dict["consent_statement"] = consent_statement
        if date_added is not UNSET:
            field_dict["date_added"] = date_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_constituent_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_id = _parse_constituent_id(d.pop("constituent_id", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _channel = d.pop("channel", UNSET)
        channel: ConstituentConsentReadChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = ConstituentConsentReadChannel(_channel)

        def _parse_inactive(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        inactive = _parse_inactive(d.pop("inactive", UNSET))

        _date = d.pop("date", UNSET)
        date: datetime.datetime | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        _response = d.pop("response", UNSET)
        response: ConstituentConsentReadResponse | Unset
        if isinstance(_response, Unset):
            response = UNSET
        else:
            response = ConstituentConsentReadResponse(_response)

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_category_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category_id = _parse_category_id(d.pop("category_id", UNSET))

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

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        constituent_consent_read = cls(
            constituent_id=constituent_id,
            id=id,
            channel=channel,
            inactive=inactive,
            date=date,
            response=response,
            category=category,
            category_id=category_id,
            source=source,
            privacy_notice=privacy_notice,
            consent_statement=consent_statement,
            date_added=date_added,
        )

        return constituent_consent_read
