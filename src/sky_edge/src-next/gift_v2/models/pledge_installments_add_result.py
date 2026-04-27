from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="PledgeInstallmentsAddResult")


@_attrs_define
class PledgeInstallmentsAddResult:
    """Represents the result of adding installments to a pledge.

    Attributes:
        installments_added (list[str] | None | Unset): A collection of identifiers of the pledge installments added to a
            pledge gift.
    """

    installments_added: list[str] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        installments_added: list[str] | None | Unset
        if isinstance(self.installments_added, Unset):
            installments_added = UNSET
        elif isinstance(self.installments_added, list):
            installments_added = self.installments_added

        else:
            installments_added = self.installments_added

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if installments_added is not UNSET:
            field_dict["installments_added"] = installments_added

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_installments_added(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                installments_added_type_0 = cast(list[str], data)

                return installments_added_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        installments_added = _parse_installments_added(d.pop("installments_added", UNSET))

        pledge_installments_add_result = cls(
            installments_added=installments_added,
        )

        return pledge_installments_add_result
