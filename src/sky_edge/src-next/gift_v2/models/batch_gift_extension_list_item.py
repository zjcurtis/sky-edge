from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.extension_exception import ExtensionException


T = TypeVar("T", bound="BatchGiftExtensionListItem")


@_attrs_define
class BatchGiftExtensionListItem:
    """Summary of an extension document for display in the batch gift list.

    Attributes:
        extension_id (None | str | Unset): The unique extension type identifier.
        display (None | str | Unset): Display label for the extension.
        exceptions (list[ExtensionException] | None | Unset): Validation exceptions reported by the extension service.
        e_tag (None | str | Unset): The ETag of the extension document for optimistic concurrency.
    """

    extension_id: None | str | Unset = UNSET
    display: None | str | Unset = UNSET
    exceptions: list[ExtensionException] | None | Unset = UNSET
    e_tag: None | str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        extension_id: None | str | Unset
        if isinstance(self.extension_id, Unset):
            extension_id = UNSET
        else:
            extension_id = self.extension_id

        display: None | str | Unset
        if isinstance(self.display, Unset):
            display = UNSET
        else:
            display = self.display

        exceptions: list[dict[str, Any]] | None | Unset
        if isinstance(self.exceptions, Unset):
            exceptions = UNSET
        elif isinstance(self.exceptions, list):
            exceptions = []
            for exceptions_type_0_item_data in self.exceptions:
                exceptions_type_0_item = exceptions_type_0_item_data.to_dict()
                exceptions.append(exceptions_type_0_item)

        else:
            exceptions = self.exceptions

        e_tag: None | str | Unset
        if isinstance(self.e_tag, Unset):
            e_tag = UNSET
        else:
            e_tag = self.e_tag

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if extension_id is not UNSET:
            field_dict["extension_id"] = extension_id
        if display is not UNSET:
            field_dict["display"] = display
        if exceptions is not UNSET:
            field_dict["exceptions"] = exceptions
        if e_tag is not UNSET:
            field_dict["e_tag"] = e_tag

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.extension_exception import ExtensionException

        d = dict(src_dict)

        def _parse_extension_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        extension_id = _parse_extension_id(d.pop("extension_id", UNSET))

        def _parse_display(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display = _parse_display(d.pop("display", UNSET))

        def _parse_exceptions(data: object) -> list[ExtensionException] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                exceptions_type_0 = []
                _exceptions_type_0 = data
                for exceptions_type_0_item_data in _exceptions_type_0:
                    exceptions_type_0_item = ExtensionException.from_dict(exceptions_type_0_item_data)

                    exceptions_type_0.append(exceptions_type_0_item)

                return exceptions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ExtensionException] | None | Unset, data)

        exceptions = _parse_exceptions(d.pop("exceptions", UNSET))

        def _parse_e_tag(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        e_tag = _parse_e_tag(d.pop("e_tag", UNSET))

        batch_gift_extension_list_item = cls(
            extension_id=extension_id,
            display=display,
            exceptions=exceptions,
            e_tag=e_tag,
        )

        return batch_gift_extension_list_item
