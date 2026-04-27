from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..models.batch_gift_custom_field_read_custom_field_data_type import BatchGiftCustomFieldReadCustomFieldDataType
from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchGiftCustomFieldRead")


@_attrs_define
class BatchGiftCustomFieldRead:
    """Represents a sing custom field on a batch record.

    Attributes:
        id (None | str | Unset): ID of the batch gift custom field
        batch_gift_id (None | str | Unset): ID of the batch gift to which this custom field belongs
        batch_id (None | str | Unset): ID of the batch to which this custom field belongs
        text_value (None | str | Unset): Text value of a text or fuzzy date custom field
        numeric_value (int | None | Unset): Numeric value of a numeric custom field
        date_value (datetime.datetime | None | Unset): Date value of a date custom field
        currency_value (float | None | Unset): Currency value of a currency custom field
        boolean_value (bool | None | Unset): Boolean value of a boolean custom field
        table_entry_id_value (int | None | Unset): Table entry ID of a table custom field
        table_entry_value (None | str | Unset): Long description of a table value custom field
        constituent_id_value (int | None | Unset): Constituent ID of a constituent custom field
        constituent_name_value (None | str | Unset): Name of the constituent, if this is a constituent type field
        data_type (BatchGiftCustomFieldReadCustomFieldDataType | Unset): Data type of the custom field
        sequence (int | None | Unset): Sequence of this custom field within the gift
        category (None | str | Unset): The category ID, foreign key to ATTRIBUTETYPES. Example: 6666.
        comment (None | str | Unset): The comment. Example: Comment.
        date (datetime.datetime | None | Unset): The date.
        description (None | str | Unset): The value of the custom field. This is the string-encoded value, its actual
            type will need to be parsed based on the type of the category. Example: Custom field description.
    """

    id: None | str | Unset = UNSET
    batch_gift_id: None | str | Unset = UNSET
    batch_id: None | str | Unset = UNSET
    text_value: None | str | Unset = UNSET
    numeric_value: int | None | Unset = UNSET
    date_value: datetime.datetime | None | Unset = UNSET
    currency_value: float | None | Unset = UNSET
    boolean_value: bool | None | Unset = UNSET
    table_entry_id_value: int | None | Unset = UNSET
    table_entry_value: None | str | Unset = UNSET
    constituent_id_value: int | None | Unset = UNSET
    constituent_name_value: None | str | Unset = UNSET
    data_type: BatchGiftCustomFieldReadCustomFieldDataType | Unset = UNSET
    sequence: int | None | Unset = UNSET
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

        text_value: None | str | Unset
        if isinstance(self.text_value, Unset):
            text_value = UNSET
        else:
            text_value = self.text_value

        numeric_value: int | None | Unset
        if isinstance(self.numeric_value, Unset):
            numeric_value = UNSET
        else:
            numeric_value = self.numeric_value

        date_value: None | str | Unset
        if isinstance(self.date_value, Unset):
            date_value = UNSET
        elif isinstance(self.date_value, datetime.datetime):
            date_value = self.date_value.isoformat()
        else:
            date_value = self.date_value

        currency_value: float | None | Unset
        if isinstance(self.currency_value, Unset):
            currency_value = UNSET
        else:
            currency_value = self.currency_value

        boolean_value: bool | None | Unset
        if isinstance(self.boolean_value, Unset):
            boolean_value = UNSET
        else:
            boolean_value = self.boolean_value

        table_entry_id_value: int | None | Unset
        if isinstance(self.table_entry_id_value, Unset):
            table_entry_id_value = UNSET
        else:
            table_entry_id_value = self.table_entry_id_value

        table_entry_value: None | str | Unset
        if isinstance(self.table_entry_value, Unset):
            table_entry_value = UNSET
        else:
            table_entry_value = self.table_entry_value

        constituent_id_value: int | None | Unset
        if isinstance(self.constituent_id_value, Unset):
            constituent_id_value = UNSET
        else:
            constituent_id_value = self.constituent_id_value

        constituent_name_value: None | str | Unset
        if isinstance(self.constituent_name_value, Unset):
            constituent_name_value = UNSET
        else:
            constituent_name_value = self.constituent_name_value

        data_type: str | Unset = UNSET
        if not isinstance(self.data_type, Unset):
            data_type = self.data_type.value

        sequence: int | None | Unset
        if isinstance(self.sequence, Unset):
            sequence = UNSET
        else:
            sequence = self.sequence

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
        if text_value is not UNSET:
            field_dict["text_value"] = text_value
        if numeric_value is not UNSET:
            field_dict["numeric_value"] = numeric_value
        if date_value is not UNSET:
            field_dict["date_value"] = date_value
        if currency_value is not UNSET:
            field_dict["currency_value"] = currency_value
        if boolean_value is not UNSET:
            field_dict["boolean_value"] = boolean_value
        if table_entry_id_value is not UNSET:
            field_dict["table_entry_id_value"] = table_entry_id_value
        if table_entry_value is not UNSET:
            field_dict["table_entry_value"] = table_entry_value
        if constituent_id_value is not UNSET:
            field_dict["constituent_id_value"] = constituent_id_value
        if constituent_name_value is not UNSET:
            field_dict["constituent_name_value"] = constituent_name_value
        if data_type is not UNSET:
            field_dict["data_type"] = data_type
        if sequence is not UNSET:
            field_dict["sequence"] = sequence
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

        def _parse_text_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        text_value = _parse_text_value(d.pop("text_value", UNSET))

        def _parse_numeric_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        numeric_value = _parse_numeric_value(d.pop("numeric_value", UNSET))

        def _parse_date_value(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_value_type_0 = isoparse(data)

                return date_value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        date_value = _parse_date_value(d.pop("date_value", UNSET))

        def _parse_currency_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        currency_value = _parse_currency_value(d.pop("currency_value", UNSET))

        def _parse_boolean_value(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        boolean_value = _parse_boolean_value(d.pop("boolean_value", UNSET))

        def _parse_table_entry_id_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        table_entry_id_value = _parse_table_entry_id_value(d.pop("table_entry_id_value", UNSET))

        def _parse_table_entry_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        table_entry_value = _parse_table_entry_value(d.pop("table_entry_value", UNSET))

        def _parse_constituent_id_value(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        constituent_id_value = _parse_constituent_id_value(d.pop("constituent_id_value", UNSET))

        def _parse_constituent_name_value(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        constituent_name_value = _parse_constituent_name_value(d.pop("constituent_name_value", UNSET))

        _data_type = d.pop("data_type", UNSET)
        data_type: BatchGiftCustomFieldReadCustomFieldDataType | Unset
        if isinstance(_data_type, Unset):
            data_type = UNSET
        else:
            data_type = BatchGiftCustomFieldReadCustomFieldDataType(_data_type)

        def _parse_sequence(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        sequence = _parse_sequence(d.pop("sequence", UNSET))

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

        batch_gift_custom_field_read = cls(
            id=id,
            batch_gift_id=batch_gift_id,
            batch_id=batch_id,
            text_value=text_value,
            numeric_value=numeric_value,
            date_value=date_value,
            currency_value=currency_value,
            boolean_value=boolean_value,
            table_entry_id_value=table_entry_id_value,
            table_entry_value=table_entry_value,
            constituent_id_value=constituent_id_value,
            constituent_name_value=constituent_name_value,
            data_type=data_type,
            sequence=sequence,
            category=category,
            comment=comment,
            date=date,
            description=description,
        )

        return batch_gift_custom_field_read
