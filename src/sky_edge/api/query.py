from datetime import datetime
from enum import StrEnum
from typing import Annotated

from pydantic import BaseModel, Field
from requests import Response

from ..util import HttpMethods, api_request


class Product(StrEnum):
    RE = "RE"
    FE = "FE"


class Module(StrEnum):
    NONE = "None"
    GENERAL_LEDGER = "GeneralLedger"
    ACCOUNTS_PAYABLE = "AccountsPayable"
    ACCOUNTS_RECEIVABLE = "AccountsReceivable"
    FIXED_ASSETS = "FixedAssets"
    CASH_RECEIPTS = "CashReceipts"


class QueryJobStatus(StrEnum):
    PENDING = "Pending"
    RUNNING = "Running"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLING = "Cancelling"
    CANCELLED = "Cancelled"
    THROTTLED = "Throttled"


class UxMode(StrEnum):
    SYNCHRONOUS = "Synchronous"
    ASYNCHRONOUS = "Asynchronous"


class OutputFormat(StrEnum):
    CSV = "Csv"
    JSON = "Json"
    JSONL = "Jsonl"
    XLSX = "Xlsx"


class FormattingMode(StrEnum):
    NONE = "None"
    UI = "UI"
    EXPORT = "Export"


class SqlGenerationMode(StrEnum):
    QUERY = "Query"
    EXPORT = "Export"
    REPORT = "Report"


class FilterOperator(StrEnum):
    EQUALS = "Equals"
    DOES_NOT_EQUAL = "DoesNotEqual"
    GREATER_THAN = "GreaterThan"
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    LESS_THAN = "LessThan"
    LESS_THAN_OR_EQUAL_TO = "LessThanOrEqualTo"
    ONE_OF = "OneOf"
    NOT_ONE_OF = "NotOneOf"
    BETWEEN = "Between"
    NOT_BETWEEN = "NotBetween"
    BEGINS_WITH = "BeginsWith"
    DOES_NOT_BEGIN_WITH = "DoesNotBeginWith"
    CONTAINS = "Contains"
    DOES_NOT_CONTAIN = "DoesNotContain"
    LIKE = "Like"
    NOT_LIKE = "NotLike"
    BLANK = "Blank"
    NOT_BLANK = "NotBlank"
    ASK = "Ask"
    SOUNDS_LIKE = "SoundsLike"
    ANY = "Any"
    ONE_OF_EACH = "OneOfEach"


class IncludeReadUrl(StrEnum):
    NEVER = "Never"
    ONCE_RUNNING = "OnceRunning"
    ONCE_COMPLETED = "OnceCompleted"


class ContentDisposition(StrEnum):
    INLINE = "Inline"
    ATTACHMENT = "Attachment"


class QueryCategory(BaseModel):
    id: int | None = None
    name: str | None = None
    sequence: int | None = None


class GetQueryCategoriesResponse(BaseModel):
    categories: list[QueryCategory] | None = None


class QuerySummary(BaseModel):
    id: int | None = None
    type: str | None = None
    added_by: str | None = None
    date_added: datetime | None = None
    last_changed_by: str | None = None
    date_changed: datetime | None = None
    select_from_query_name: str | None = None
    category: str | None = None
    query_list: bool | None = None
    can_modify: bool | None = None
    can_execute: bool | None = None
    view_supported: bool | None = None
    edit_supported: bool | None = None
    supported_execution_modes: str | None = None
    favorite: bool | None = None
    created_by_query: bool | None = None
    has_ask_fields: bool | None = None
    name: str | None = None


class GetQueryListResponse(BaseModel):
    queries: list[QuerySummary] | None = None
    any_query_types: bool | None = None
    count: int | None = None
    limit: int
    offset: int


class AskFieldInformation(BaseModel):
    filter_values: list | None = None
    operator: FilterOperator | None = None


class ExecuteQueryByIdRequest(BaseModel):
    id: int
    ux_mode: UxMode = UxMode.ASYNCHRONOUS
    output_format: OutputFormat = OutputFormat.CSV
    formatting_mode: FormattingMode = FormattingMode.NONE
    sql_generation_mode: SqlGenerationMode = SqlGenerationMode.QUERY
    use_static_query_id_set: bool = False
    results_file_name: str | None = None
    ask_fields: list[AskFieldInformation] | None = None
    display_code_table_long_description: bool = False
    time_zone_offset_in_minutes: int | None = None


class ExecuteQueryResponse(BaseModel):
    id: str
    status: QueryJobStatus | None = None
    message: str | None = None


class QueryExecutionJob(BaseModel):
    id: str | None = None
    status: QueryJobStatus | None = None
    sas_uri: str | None = None
    row_count: int | None = None

    def fetch_content(self) -> Response:
        """Fetches the query results from the sas_uri.

        Returns:
            Response object containing the query results.

        Raises:
            ValueError: If sas_uri is None or empty.
        """
        if not self.sas_uri:
            raise ValueError(
                "sas_uri is not available. The job may not be completed yet."
            )

        return api_request(
            method=HttpMethods.GET,
            url=self.sas_uri,
            drop_headers=True,
        )


class QueryListQuery(BaseModel):
    product: Product
    module: Module
    offset: int | None = None
    query_type_id: int | None = None
    category: int | None = None
    limit: Annotated[int, Field(ge=1, le=200)] | None = None
    search_text: Annotated[str, Field(max_length=60)] | None = None
    merged_queries_only: bool | None = None
    my_queries_only: bool | None = None


def query_categories_get(
    product: Product, module: Module
) -> GetQueryCategoriesResponse | Response:
    """Gets query categories.

    Args:
        product: The Blackbaud product (RE or FE)
        module: The module (RE must use 'None')

    Returns:
        GetQueryCategoriesResponse or Response if error
    """
    params = {"product": product, "module": module}
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/query/categories",
        params=params,
        response_model=GetQueryCategoriesResponse,
    )


def query_list_get(query: QueryListQuery) -> GetQueryListResponse | Response:
    """Gets a list of queries.

    Args:
        query: QueryListQuery with filter parameters

    Returns:
        GetQueryListResponse or Response if error
    """
    return api_request(
        method=HttpMethods.GET,
        url="https://api.sky.blackbaud.com/query/queries",
        params=query.model_dump(exclude_none=True),
        response_model=GetQueryListResponse,
    )


def query_execution_job_by_id_post(
    product: Product, module: Module, request: ExecuteQueryByIdRequest
) -> ExecuteQueryResponse | Response:
    """Creates a background job to execute a query specified by ID.

    Args:
        product: The Blackbaud product (RE or FE)
        module: The module (RE must use 'None')
        request: ExecuteQueryByIdRequest with query execution parameters

    Returns:
        ExecuteQueryResponse or Response if error
    """
    params = {"product": product, "module": module}
    return api_request(
        method=HttpMethods.POST,
        url="https://api.sky.blackbaud.com/query/queries/executebyid",
        params=params,
        data=request.model_dump_json(exclude_none=True),
        response_model=ExecuteQueryResponse,
    )


def query_execution_job_status_get(
    job_id: str,
    product: Product,
    module: Module,
    include_read_url: IncludeReadUrl | None = None,
    content_disposition: ContentDisposition | None = None,
) -> QueryExecutionJob | Response:
    """Gets information about a background query execution job.

    Args:
        job_id: The job ID returned from the POST Query execution job request
        product: The Blackbaud product (RE or FE)
        module: The module (RE must use 'None')
        include_read_url: When to include the SAS URL in the response
        content_disposition: Content disposition for the SAS URL

    Returns:
        QueryExecutionJob or Response if error
    """
    params = {"product": product, "module": module}
    if include_read_url:
        params["include_read_url"] = include_read_url
    if content_disposition:
        params["content_disposition"] = content_disposition

    return api_request(
        method=HttpMethods.GET,
        url=f"https://api.sky.blackbaud.com/query/jobs/{job_id}",
        params=params,
        response_model=QueryExecutionJob,
    )
