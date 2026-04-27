from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from sky_edge.next.types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.constituent_search_result import ConstituentSearchResult


T = TypeVar("T", bound="ConstituentCollection")


@_attrs_define
class ConstituentCollection:
    """Defines a collection of constituent list entries.

    Attributes:
        results (list[ConstituentSearchResult] | None | Unset): The set of items included in the response. This may be a
            subset of the items in the collection.
    """

    results: list[ConstituentSearchResult] | None | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        results: list[dict[str, Any]] | None | Unset
        if isinstance(self.results, Unset):
            results = UNSET
        elif isinstance(self.results, list):
            results = []
            for results_type_0_item_data in self.results:
                results_type_0_item = results_type_0_item_data.to_dict()
                results.append(results_type_0_item)

        else:
            results = self.results

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.constituent_search_result import ConstituentSearchResult

        d = dict(src_dict)

        def _parse_results(
            data: object,
        ) -> list[ConstituentSearchResult] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                results_type_0 = []
                _results_type_0 = data
                for results_type_0_item_data in _results_type_0:
                    results_type_0_item = ConstituentSearchResult.from_dict(
                        results_type_0_item_data
                    )

                    results_type_0.append(results_type_0_item)

                return results_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ConstituentSearchResult] | None | Unset, data)

        results = _parse_results(d.pop("results", UNSET))

        constituent_collection = cls(
            results=results,
        )

        return constituent_collection
