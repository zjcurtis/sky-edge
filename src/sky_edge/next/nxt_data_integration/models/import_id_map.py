from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

T = TypeVar("T", bound="ImportIdMap")


@_attrs_define
class ImportIdMap:
    """A mapping between a system record ID and an import ID.

    Attributes:
        import_id (None | str | Unset): The Import ID.
        system_record_id (int | Unset): The system record ID.
    """

    import_id: None | str | Unset = UNSET
    system_record_id: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        import_id: None | str | Unset
        if isinstance(self.import_id, Unset):
            import_id = UNSET
        else:
            import_id = self.import_id

        system_record_id = self.system_record_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if import_id is not UNSET:
            field_dict["import_id"] = import_id
        if system_record_id is not UNSET:
            field_dict["system_record_id"] = system_record_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_import_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        import_id = _parse_import_id(d.pop("import_id", UNSET))

        system_record_id = d.pop("system_record_id", UNSET)

        import_id_map = cls(
            import_id=import_id,
            system_record_id=system_record_id,
        )

        return import_id_map
