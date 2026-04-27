from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryWriteErrorCodes")


@_attrs_define
class QueryWriteErrorCodes:
    """A machine-readable format for specifying errors in HTTP API responses based on https://tools.ietf.org/html/rfc7807.

    Attributes:
        type_ (None | str | Unset): A URI reference [RFC3986] that identifies the problem type. This specification
            encourages that, when dereferenced, it provide human-readable documentation for the problem type (e.g., using
            HTML [W3C.REC-html5-20141028]). When this member is not present, its value is assumed to be
            "about:blank".<br/><br/>Available
            values:<table><tr><th>type</th><th>detail</th></tr><tr><td>urn:blackbaud:model-validation-error</td><td>A model
            validation rule was violated, such as a missing required field.</td></tr><tr><td>urn:blackbaud:missing-
            product</td><td>Product was not supplied.</td></tr><tr><td>urn:blackbaud:invalid-product</td><td>Supplied
            product is invalid.</td></tr><tr><td>urn:blackbaud:invalid-module</td><td>Supplied module is
            invalid.</td></tr><tr><td>urn:blackbaud:invalid-module-for-product</td><td>Module {0} is not valid for product
            {1}</td></tr><tr><td>urn:blackbaud:invalid-type-id</td><td>Invalid query
            type.</td></tr><tr><td>urn:blackbaud:property-not-supported</td><td>The property '{0}' is not yet supported on
            this operation.</td></tr><tr><td>urn:blackbaud:query-name-must-be-unique</td><td>Query name must be
            unique.</td></tr><tr><td>urn:blackbaud:invalid-category</td><td>Invalid query
            category.</td></tr><tr><td>urn:blackbaud:select-from-query-must-exist-and-be-of-same-type</td><td>Select from
            query ID must exist and be of the same query type.</td></tr><tr><td>urn:blackbaud:query-field-is-of-incorrect-
            query-type</td><td>The provided query field {0} (ID: {1}) in {2} cannot be used with the query type
            {3}.</td></tr><tr><td>urn:blackbaud:unbalanced-filter-parentheses</td><td>The provided filter fields {0}have an
            invalid number and/or order of parentheses.</td></tr><tr><td>urn:blackbaud:filter-value-count-invalid-for-
            filter-operator</td><td>The provided number of filter values {0} are invalid for the provided filter_operator
            {1} at {2}.</td></tr><tr><td>urn:blackbaud:invalid-filter-values-for-fegl-date</td><td>The provided filter
            values for the FE GL date filter field are invalid.</td></tr><tr><td>urn:blackbaud:invalid-filter-
            operator</td><td>The operator {0} for {1} is not valid for {2}.</td></tr><tr><td>urn:blackbaud:invalid-query-
            field-id</td><td>Query field {0} referenced at {1} does not exist.</td></tr><tr><td>urn:blackbaud:output-limit-
            not-allowed</td><td>Output limits can only be set for static queries.</td></tr><tr><td>urn:blackbaud:add-edit-
            unsupported</td><td>Query field {0} referenced at {1} does not currently support add, edit, or ad-hoc
            execution.</td></tr><tr><td>urn:blackbaud:invalid-compare-type</td><td>The compare_type must be None for the
            first filter field, and And or Or for all others.</td></tr><tr><td>urn:blackbaud:invalid-filter-
            value</td><td>The value '{0}' at {1} is not a valid {2} value.</td></tr><tr><td>urn:blackbaud:invalid-int-
            filter-value</td><td>The value '{0}' at {1} is not a valid {2} value. A positive, non-zero integer is
            expected.</td></tr><tr><td>urn:blackbaud:soft-credit-sub-option-mismatch</td><td>Soft credit sub-option is only
            applicable to soft credit option 'Recipients' and 'Both'.</td></tr><tr><td>urn:blackbaud:use-gross-amount-for-
            covenants-not-allowed</td><td>Use gross amount for covenants is not allowed for the environment's
            country.</td></tr><tr><td>urn:blackbaud:invalid-date-range</td><td>Invalid date range for
            {0}.</td></tr><tr><td>urn:blackbaud:wildcard-required</td><td>The {0} operator requires a wildcard character in
            the filter value.</td></tr><tr><td>urn:blackbaud:missing-unique-id</td><td>Unique ID is required for query field
            {0} referenced at {1}.</td></tr><tr><td>urn:blackbaud:invalid-unique-id</td><td>Unique ID {0} is not valid for
            query field {1} referenced at {2}.</td></tr><tr><td>urn:blackbaud:invalid-sum-instance</td><td>Summary instance
            {0} is not valid at {1}.</td></tr><tr><td>urn:blackbaud:invalid-sum-instance-in-filter-field</td><td>Invalid
            summary instance in filter fields at {0}. Filter fields on a summary field must either have no summary instance
            or have the same summary instance as the parent summary field.</td></tr><tr><td>urn:blackbaud:invalid-filter-
            field-on-summary</td><td>The filter field at {0} is not available for summary field
            {1}.</td></tr><tr><td>urn:blackbaud:invalid-default-filter-field-on-summary</td><td>The filter field at {0} did
            not match the expected default filter field for summary field {1}.</td></tr><tr><td>urn:blackbaud:invalid-
            sequence-value</td><td>{0} is not a valid sequence value for an address processing
            filter.</td></tr><tr><td>urn:blackbaud:invalid-product-for-property</td><td>{0} is not valid for {1}
            queries.</td></tr><tr><td>urn:blackbaud:invalid-address-type-for-address-processing</td><td>{0} is an invalid
            address type for {1} address processing {2}. </td></tr><tr><td>urn:blackbaud:specific-address-id-
            required</td><td>Address processing filters with specific address type require a specific address type ID.
            </td></tr><tr><td>urn:blackbaud:specific-address-type-required</td><td>Address processing filters with specific
            address IDs require a specific address type. </td></tr><tr><td>urn:blackbaud:invalid-duplicate-sort-
            field</td><td>Sort field values must be unique within the sort fields
            collection.</td></tr><tr><td>urn:blackbaud:head-of-household-processing-requires-single-row-
            layout</td><td>head_of_household_option is not supported for multi-row result layout
            queries.</td></tr><tr><td>urn:blackbaud:required-field</td><td>The required field '{0}' does not have a
            value.</td></tr><tr><td>urn:blackbaud:null-collection-item</td><td>One or more items in the '{0}' collection are
            null.</td></tr><tr><td>urn:blackbaud:duplicate-values</td><td>The '{0}' collection has duplicate
            values.</td></tr><tr><td>urn:blackbaud:invalid-value</td><td>'{0}' is not a valid value for
            {1}.</td></tr><tr><td>urn:blackbaud:invalid-string-length</td><td>The value provided for {0} must be {1}
            characters or less.</td></tr><tr><td>urn:blackbaud:invalid-integer-value</td><td>{0} is not a valid value for
            {1}.</td></tr><tr><td>urn:blackbaud:empty-or-white-space-value</td><td>The field '{0}' is empty or
            whitespace.</td></tr><tr><td>urn:blackbaud:flexible-date-not-valid</td><td>The flexible date field '{0}' is not
            valid.</td></tr></table>
        title (None | str | Unset): A short, human-readable summary of the problem type. It SHOULD NOT change from
            occurrence to occurrence of the problem, except for purposes of localization (e.g., using proactive content
            negotiation; see [RFC7231], Section 3.4).
        status (int | None | Unset): The HTTP status code ([RFC7231], Section 6) generated by the origin server for this
            occurrence of the problem.
        detail (None | str | Unset): A human-readable explanation specific to this occurrence of the problem.
        instance (None | str | Unset): A URI reference that identifies the specific occurrence of the problem. It may or
            may not yield further information if dereferenced.
        trace_id (str | Unset): A request ID that can be provided to Blackbaud Support that may help with further
            troubleshooting.
        span_id (str | Unset): A request ID that can be provided to Blackbaud Support that may help with further
            troubleshooting.
    """

    type_: None | str | Unset = UNSET
    title: None | str | Unset = UNSET
    status: int | None | Unset = UNSET
    detail: None | str | Unset = UNSET
    instance: None | str | Unset = UNSET
    trace_id: str | Unset = UNSET
    span_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        status: int | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        else:
            status = self.status

        detail: None | str | Unset
        if isinstance(self.detail, Unset):
            detail = UNSET
        else:
            detail = self.detail

        instance: None | str | Unset
        if isinstance(self.instance, Unset):
            instance = UNSET
        else:
            instance = self.instance

        trace_id = self.trace_id

        span_id = self.span_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if title is not UNSET:
            field_dict["title"] = title
        if status is not UNSET:
            field_dict["status"] = status
        if detail is not UNSET:
            field_dict["detail"] = detail
        if instance is not UNSET:
            field_dict["instance"] = instance
        if trace_id is not UNSET:
            field_dict["trace_id"] = trace_id
        if span_id is not UNSET:
            field_dict["span_id"] = span_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_status(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_detail(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        detail = _parse_detail(d.pop("detail", UNSET))

        def _parse_instance(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        instance = _parse_instance(d.pop("instance", UNSET))

        trace_id = d.pop("trace_id", UNSET)

        span_id = d.pop("span_id", UNSET)

        query_write_error_codes = cls(
            type_=type_,
            title=title,
            status=status,
            detail=detail,
            instance=instance,
            trace_id=trace_id,
            span_id=span_id,
        )

        query_write_error_codes.additional_properties = d
        return query_write_error_codes

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
