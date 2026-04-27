from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.gift_validation_error import GiftValidationError


T = TypeVar("T", bound="GiftValidationErrors")


@_attrs_define
class GiftValidationErrors:
    """Collection of gift validation errors

    Attributes:
        errors (list[GiftValidationError] | None | Unset): The gift validation errors encountered by the endpoint
    """

    errors: list[GiftValidationError] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        errors: list[dict[str, Any]] | None | Unset
        if isinstance(self.errors, Unset):
            errors = UNSET
        elif isinstance(self.errors, list):
            errors = []
            for errors_type_0_item_data in self.errors:
                errors_type_0_item = errors_type_0_item_data.to_dict()
                errors.append(errors_type_0_item)

        else:
            errors = self.errors

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.gift_validation_error import GiftValidationError

        d = dict(src_dict)

        def _parse_errors(data: object) -> list[GiftValidationError] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                errors_type_0 = []
                _errors_type_0 = data
                for errors_type_0_item_data in _errors_type_0:
                    errors_type_0_item = GiftValidationError.from_dict(
                        errors_type_0_item_data
                    )

                    errors_type_0.append(errors_type_0_item)

                return errors_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[GiftValidationError] | None | Unset, data)

        errors = _parse_errors(d.pop("errors", UNSET))

        gift_validation_errors = cls(
            errors=errors,
        )

        return gift_validation_errors
