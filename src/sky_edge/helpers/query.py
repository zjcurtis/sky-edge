from time import sleep

from sky_edge.api.query import (
    ExecuteQueryByIdRequest,
    ExecuteQueryResponse,
    GetQueryCategoriesResponse,
    GetQueryListResponse,
    IncludeReadUrl,
    Module,
    Product,
    QueryExecutionJob,
    QueryJobStatus,
    QueryListQuery,
    UxMode,
    query_categories_get,
    query_execution_job_by_id_post,
    query_execution_job_status_get,
    query_list_get,
)


def get_query_id_by_category_and_name(category: str, name: str) -> int | None:
    category_list = query_categories_get(product=Product.RE, module=Module.NONE)
    if (
        isinstance(category_list, GetQueryCategoriesResponse)
        and category_list.categories
    ):
        for cat in category_list.categories:
            if cat.name == category:
                my_id = cat.id
                my_query = QueryListQuery(
                    product=Product.RE,
                    module=Module.NONE,
                    category=my_id,
                )
                query_response = query_list_get(my_query)
                if (
                    isinstance(query_response, GetQueryListResponse)
                    and query_response.queries
                ):
                    for query in query_response.queries:
                        if query.name == name and query.id:
                            return query.id


def execute_query_by_name(id: int) -> bytes | None:
    query_post_response = query_execution_job_by_id_post(
        Product.RE,
        module=Module.NONE,
        request=ExecuteQueryByIdRequest(
            id=id,
            ux_mode=UxMode.SYNCHRONOUS,
        ),
    )
    if isinstance(query_post_response, ExecuteQueryResponse):
        if query_post_response.status != QueryJobStatus.CANCELLED:
            job_status = query_execution_job_status_get(
                job_id=query_post_response.id,
                product=Product.RE,
                module=Module.NONE,
                include_read_url=IncludeReadUrl.ONCE_COMPLETED,
            )
            if isinstance(job_status, QueryExecutionJob):
                while job_status.status != QueryJobStatus.COMPLETED:
                    sleep(9)
                    job_status = query_execution_job_status_get(
                        job_id=query_post_response.id,
                        product=Product.RE,
                        module=Module.NONE,
                        include_read_url=IncludeReadUrl.ONCE_COMPLETED,
                    )
                if isinstance(job_status, QueryExecutionJob):
                    fetched_response = job_status.fetch_content()
                    if fetched_response.status_code == 200:
                        return fetched_response.content
