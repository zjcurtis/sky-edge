from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_table_entry import CodeTableEntry


T = TypeVar("T", bound="MembershipDrop")


@_attrs_define
class MembershipDrop:
    """Membership drop request model

    Attributes:
        drop_date (datetime.date): The drop date of the transaction.
        reason (CodeTableEntry): A predefined entry in a code table.
        mem_comment (None | str | Unset): Gets or sets value of comment.
    """

    drop_date: datetime.date
    reason: CodeTableEntry
    mem_comment: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        drop_date = self.drop_date.isoformat()

        reason = self.reason.to_dict()

        mem_comment: None | str | Unset
        if isinstance(self.mem_comment, Unset):
            mem_comment = UNSET
        else:
            mem_comment = self.mem_comment

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "drop_date": drop_date,
                "reason": reason,
            }
        )
        if mem_comment is not UNSET:
            field_dict["mem_comment"] = mem_comment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.code_table_entry import CodeTableEntry

        d = dict(src_dict)
        drop_date = isoparse(d.pop("drop_date")).date()

        reason = CodeTableEntry.from_dict(d.pop("reason"))

        def _parse_mem_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mem_comment = _parse_mem_comment(d.pop("mem_comment", UNSET))

        membership_drop = cls(
            drop_date=drop_date,
            reason=reason,
            mem_comment=mem_comment,
        )

        return membership_drop
