from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="EmailAddressRead")


@_attrs_define
class EmailAddressRead:
    """Email addresses store information about constituent email accounts and where to send email correspondences for
    individuals and organizations.

        Attributes:
            id (str | Unset): The immutable system record ID of the email address.
            address (str | Unset): The email address.
            constituent_id (str | Unset): The immutable system record ID of the constituent associated with the email
                address.
            date_added (datetime.datetime | Unset): The date when the email address was created. Includes an offset from UTC
                in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            date_modified (datetime.datetime | Unset): The date when the email address was last modified. Includes an offset
                from UTC in <a href="https://tools.ietf.org/html/rfc3339">ISO-8601 format: </a><i>1969-11-21T10:29:43-04:00</i>.
            do_not_email (bool | Unset): Indicates whether the constituent requests not to be contacted at this email
                address.
            inactive (bool | Unset): Indicates whether the email address is inactive.
            primary (bool | Unset): Indicates whether this is the constituent's primary email address.
            type_ (str | Unset): The type of email address. Available values are the entries in the <a href="https://develop
                er.sky.blackbaud.com/docs/services/56b76470069a0509c8f1c5b3/operations/ListEmailAddressTypes"><b>Phone
                Types</b></a> table.
    """

    id: str | Unset = UNSET
    address: str | Unset = UNSET
    constituent_id: str | Unset = UNSET
    date_added: datetime.datetime | Unset = UNSET
    date_modified: datetime.datetime | Unset = UNSET
    do_not_email: bool | Unset = UNSET
    inactive: bool | Unset = UNSET
    primary: bool | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        address = self.address

        constituent_id = self.constituent_id

        date_added: str | Unset = UNSET
        if not isinstance(self.date_added, Unset):
            date_added = self.date_added.isoformat()

        date_modified: str | Unset = UNSET
        if not isinstance(self.date_modified, Unset):
            date_modified = self.date_modified.isoformat()

        do_not_email = self.do_not_email

        inactive = self.inactive

        primary = self.primary

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if address is not UNSET:
            field_dict["address"] = address
        if constituent_id is not UNSET:
            field_dict["constituent_id"] = constituent_id
        if date_added is not UNSET:
            field_dict["date_added"] = date_added
        if date_modified is not UNSET:
            field_dict["date_modified"] = date_modified
        if do_not_email is not UNSET:
            field_dict["do_not_email"] = do_not_email
        if inactive is not UNSET:
            field_dict["inactive"] = inactive
        if primary is not UNSET:
            field_dict["primary"] = primary
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        address = d.pop("address", UNSET)

        constituent_id = d.pop("constituent_id", UNSET)

        _date_added = d.pop("date_added", UNSET)
        date_added: datetime.datetime | Unset
        if isinstance(_date_added, Unset):
            date_added = UNSET
        else:
            date_added = isoparse(_date_added)

        _date_modified = d.pop("date_modified", UNSET)
        date_modified: datetime.datetime | Unset
        if isinstance(_date_modified, Unset):
            date_modified = UNSET
        else:
            date_modified = isoparse(_date_modified)

        do_not_email = d.pop("do_not_email", UNSET)

        inactive = d.pop("inactive", UNSET)

        primary = d.pop("primary", UNSET)

        type_ = d.pop("type", UNSET)

        email_address_read = cls(
            id=id,
            address=address,
            constituent_id=constituent_id,
            date_added=date_added,
            date_modified=date_modified,
            do_not_email=do_not_email,
            inactive=inactive,
            primary=primary,
            type_=type_,
        )

        email_address_read.additional_properties = d
        return email_address_read

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
