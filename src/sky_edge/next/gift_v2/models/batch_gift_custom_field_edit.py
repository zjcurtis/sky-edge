from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="BatchGiftCustomFieldEdit")


@_attrs_define
class BatchGiftCustomFieldEdit:
    """Editable batch gift custom field

    Attributes:
        id (None | str | Unset): ID of the gift custom field
        batch_gift_id (None | str | Unset): ID of the batch gift to which this custom field belongs
        batch_id (None | str | Unset): ID of the batch to which this custom field belongs
        category (None | str | Unset): The category ID, foreign key to ATTRIBUTETYPES. Example: 6666.
        comment (None | str | Unset): The comment. Example: Comment.
        date (datetime.datetime | None | Unset): The date.
        description (None | str | Unset): The value of the custom field. This is the string-encoded value, its actual
            type will need to be parsed based on the type of the category. Example: Custom field description.
    """

    id: None | str | Unset = UNSET
    batch_gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    category: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    date: datetime.datetime | None | Unset = UNSET
    description: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        batch_gift_id: None | str | Unset
        if isinstance(self.batch_gift_id, Unset):
            batch_gift_id = UNSET
        else:
            batch_gift_id = self.batch_gift_id

        batch_id: None | str | Unset
        if isinstance(self.batch_id, Unset):
            batch_id = UNSET
        else:
            batch_id = self.batch_id

        category: None | str | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        else:
            category = self.category

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        date: None | str | Unset
        if isinstance(self.date, Unset):
            date = UNSET
        elif isinstance(self.date, datetime.datetime):
            date = self.date.isoformat()
        else:
            date = self.date

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if batch_gift_id is not UNSET:
            field_dict["batch_gift_id"] = batch_gift_id
        if batch_id is not UNSET:
            field_dict["batch_id"] = batch_id
        if category is not UNSET:
            field_dict["category"] = category
        if comment is not UNSET:
            field_dict["comment"] = comment
        if date is not UNSET:
            field_dict["date"] = date
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_batch_gift_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_gift_id = _parse_batch_gift_id(d.pop("batch_gift_id", UNSET))

        def _parse_batch_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        batch_id = _parse_batch_id(d.pop("batch_id", UNSET))

        def _parse_category(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))

        def _parse_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_type_0 = isoparse(data)

                return date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date = _parse_date(d.pop("date", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        batch_gift_custom_field_edit = cls(
            id=id,
            batch_gift_id=batch_gift_id,
            batch_id=batch_id,
            category=category,
            comment=comment,
            date=date,
            description=description,
        )

        return batch_gift_custom_field_edit
