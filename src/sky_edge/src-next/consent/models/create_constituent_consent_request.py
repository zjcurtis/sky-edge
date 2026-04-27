from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.create_constituent_consent_request_consent_response import CreateConstituentConsentRequestConsentResponse

T = TypeVar("T", bound="CreateConstituentConsentRequest")


@_attrs_define
class CreateConstituentConsentRequest:
    """Model used by SkyApi to create a consent record for a given constituent

    Attributes:
        constituent_id (str): The constituent identifier
        consent_date (datetime.datetime): Date on which the consent response was provided.
        consent_response (CreateConstituentConsentRequestConsentResponse): The consent response provided by the
            constituent.<p>Members:</p><ul><li><i>OptIn</i> - Opt-in</li><li><i>OptOut</i> - Opt-
            out</li><li><i>NoResponse</i> - No response</li></ul>
    """

    constituent_id: str
    consent_date: datetime.datetime
    consent_response: CreateConstituentConsentRequestConsentResponse

    def to_dict(self) -> dict[str, Any]:
        constituent_id = self.constituent_id

        consent_date = self.consent_date.isoformat()

        consent_response = self.consent_response.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "constituent_id": constituent_id,
                "consent_date": consent_date,
                "consent_response": consent_response,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        constituent_id = d.pop("constituent_id")

        consent_date = isoparse(d.pop("consent_date"))

        consent_response = CreateConstituentConsentRequestConsentResponse(d.pop("consent_response"))

        create_constituent_consent_request = cls(
            constituent_id=constituent_id,
            consent_date=consent_date,
            consent_response=consent_response,
        )

        return create_constituent_consent_request
