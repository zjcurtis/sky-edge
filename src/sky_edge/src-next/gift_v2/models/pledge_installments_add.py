from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.pledge_installment_add import PledgeInstallmentAdd


T = TypeVar("T", bound="PledgeInstallmentsAdd")


@_attrs_define
class PledgeInstallmentsAdd:
    """Adds multiple pledge installments to a pledge gift.

    Attributes:
        installments (list[PledgeInstallmentAdd]): A collection of installments to add to a pledge gift.
    """

    installments: list[PledgeInstallmentAdd]

    def to_dict(self) -> dict[str, Any]:
        installments = []
        for installments_item_data in self.installments:
            installments_item = installments_item_data.to_dict()
            installments.append(installments_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "installments": installments,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pledge_installment_add import PledgeInstallmentAdd

        d = dict(src_dict)
        installments = []
        _installments = d.pop("installments")
        for installments_item_data in _installments:
            installments_item = PledgeInstallmentAdd.from_dict(installments_item_data)

            installments.append(installments_item)

        pledge_installments_add = cls(
            installments=installments,
        )

        return pledge_installments_add
