from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.create_constituent_consents_request_channel import CreateConstituentConsentsRequestChannel
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_constituent_consent_request import CreateConstituentConsentRequest


T = TypeVar("T", bound="CreateConstituentConsentsRequest")


@_attrs_define
class CreateConstituentConsentsRequest:
    """Model used by SkyApi to create consent records for multiple constituents

    Attributes:
        channel (CreateConstituentConsentsRequestChannel): The name of the channel.<p>Members:</p><ul><li><i>Email</i> -
            Email</li><li><i>Mail</i> - Mail</li><li><i>SMS</i> - SMS</li><li><i>Phone</i> - Phone</li><li><i>AutoPhone</i>
            - AutoPhone</li><li><i>Social</i> - Social media</li><li><i>DataProcessing</i> - Data
            processing</li><li><i>Other</i> - Other</li></ul>
        category (None | str | Unset): The name of the category.
        source (None | str | Unset): The name of the source.
        privacy_policy (None | str | Unset): Privacy policy for consent.
        consent_statement (None | str | Unset): Consent statement for consent.
        constituent_requests (list[CreateConstituentConsentRequest] | None | Unset): Collection of create constituent
            consent requests
    """

    channel: CreateConstituentConsentsRequestChannel
    category: None | str | Unset = UNSET
    source: None | str | Unset = UNSET
    privacy_policy: None | str | Unset = UNSET
    consent_statement: None | str | Unset = UNSET
    constituent_requests: list[CreateConstituentConsentRequest] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        channel = self.channel.value

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

        constituent_requests: list[dict[str, Any]] | None | Unset
        if isinstance(self.constituent_requests, Unset):
            constituent_requests = UNSET
        elif isinstance(self.constituent_requests, list):
            constituent_requests = []
            for constituent_requests_type_0_item_data in self.constituent_requests:
                constituent_requests_type_0_item = constituent_requests_type_0_item_data.to_dict()
                constituent_requests.append(constituent_requests_type_0_item)

        else:
            constituent_requests = self.constituent_requests

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "channel": channel,
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
        if constituent_requests is not UNSET:
            field_dict["constituent_requests"] = constituent_requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_constituent_consent_request import CreateConstituentConsentRequest

        d = dict(src_dict)
        channel = CreateConstituentConsentsRequestChannel(d.pop("channel"))

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

        def _parse_constituent_requests(data: object) -> list[CreateConstituentConsentRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                constituent_requests_type_0 = []
                _constituent_requests_type_0 = data
                for constituent_requests_type_0_item_data in _constituent_requests_type_0:
                    constituent_requests_type_0_item = CreateConstituentConsentRequest.from_dict(
                        constituent_requests_type_0_item_data
                    )

                    constituent_requests_type_0.append(constituent_requests_type_0_item)

                return constituent_requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[CreateConstituentConsentRequest] | None | Unset, data)

        constituent_requests = _parse_constituent_requests(d.pop("constituent_requests", UNSET))

        create_constituent_consents_request = cls(
            channel=channel,
            category=category,
            source=source,
            privacy_policy=privacy_policy,
            consent_statement=consent_statement,
            constituent_requests=constituent_requests,
        )

        return create_constituent_consents_request
