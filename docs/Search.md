# zincsearch_sdk.Search

All URIs are relative to *http://localhost:4080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**msearch**](Search.md#msearch) | **POST** /es/_msearch | Search V2 MultipleSearch for compatible ES
[**search**](Search.md#search) | **POST** /es/{index}/_search | Search V2 DSL for compatible ES
[**search_v1**](Search.md#search_v1) | **POST** /api/{index}/_search | Search V1


# **msearch**
> MetaSearchResponse msearch(query)

Search V2 MultipleSearch for compatible ES

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import search
from zincsearch_sdk.model.meta_search_response import MetaSearchResponse
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4080
# See configuration.py for a list of all supported configuration parameters.
configuration = zincsearch_sdk.Configuration(
    host = "http://localhost:4080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = zincsearch_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with zincsearch_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search.Search(api_client)
    query = "query_example" # str | Query

    # example passing only required values which don't have defaults set
    try:
        # Search V2 MultipleSearch for compatible ES
        api_response = api_instance.msearch(query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Search->msearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

### Return type

[**MetaSearchResponse**](MetaSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> MetaSearchResponse search(index, query)

Search V2 DSL for compatible ES

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import search
from zincsearch_sdk.model.meta_zinc_query import MetaZincQuery
from zincsearch_sdk.model.meta_search_response import MetaSearchResponse
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4080
# See configuration.py for a list of all supported configuration parameters.
configuration = zincsearch_sdk.Configuration(
    host = "http://localhost:4080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = zincsearch_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with zincsearch_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search.Search(api_client)
    index = "index_example" # str | Index
    query = MetaZincQuery(
        source=[
            "source_example",
        ],
        aggs={
            "key": MetaAggregations(
                aggs={
                    "key": MetaAggregations(),
                },
                auto_date_histogram=MetaAggregationAutoDateHistogram(
                    buckets=1,
                    field="field_example",
                    format="format_example",
                    keyed=True,
                    minimum_interval="minimum_interval_example",
                    time_zone="time_zone_example",
                ),
                avg=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                cardinality=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                count=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                date_histogram=MetaAggregationDateHistogram(
                    calendar_interval="calendar_interval_example",
                    extended_bounds=AggregationHistogramBound(
                        max=3.14,
                        min=3.14,
                    ),
                    field="field_example",
                    fixed_interval="fixed_interval_example",
                    format="format_example",
                    hard_bounds=AggregationHistogramBound(
                        max=3.14,
                        min=3.14,
                    ),
                    interval="interval_example",
                    keyed=True,
                    min_doc_count=1,
                    size=1,
                    time_zone="time_zone_example",
                ),
                date_range=MetaAggregationDateRange(
                    field="field_example",
                    format="format_example",
                    keyed=True,
                    ranges=[
                        MetaDateRange(
                            _from="_from_example",
                            to="to_example",
                        ),
                    ],
                    time_zone="time_zone_example",
                ),
                histogram=MetaAggregationHistogram(
                    extended_bounds=AggregationHistogramBound(
                        max=3.14,
                        min=3.14,
                    ),
                    field="field_example",
                    hard_bounds=AggregationHistogramBound(
                        max=3.14,
                        min=3.14,
                    ),
                    interval=3.14,
                    keyed=True,
                    min_doc_count=1,
                    offset=3.14,
                    size=1,
                ),
                ip_range=MetaAggregationIPRange(
                    field="field_example",
                    keyed=True,
                    ranges=[
                        MetaIPRange(
                            _from="_from_example",
                            to="to_example",
                        ),
                    ],
                ),
                max=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                min=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                range=MetaAggregationRange(
                    field="field_example",
                    keyed=True,
                    ranges=[
                        MetaRange(
                            _from=3.14,
                            to=3.14,
                        ),
                    ],
                ),
                sum=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
                terms=MetaAggregationsTerms(
                    field="field_example",
                    order={
                        "key": "key_example",
                    },
                    size=1,
                ),
                weighted_avg=MetaAggregationMetric(
                    field="field_example",
                    weight_field="weight_field_example",
                ),
            ),
        },
        explain=True,
        fields=[
            "fields_example",
        ],
        _from=1,
        highlight=MetaHighlight(
            fields={
                "key": MetaHighlight(),
            },
            fragment_size=1,
            number_of_fragments=1,
            post_tags=[
                "post_tags_example",
            ],
            pre_tags=[
                "pre_tags_example",
            ],
        ),
        query=MetaQuery(
            bool=MetaBoolQuery(
                filter=[
                    MetaQuery(),
                ],
                minimum_should_match=3.14,
                must=[
                    MetaQuery(),
                ],
                must_not=[
                    MetaQuery(),
                ],
                should=[
                    MetaQuery(),
                ],
            ),
            exists=MetaExistsQuery(
                field="field_example",
            ),
            fuzzy={
                "key": MetaFuzzyQuery(
                    boost=3.14,
                    fuzziness={},
                    prefix_length=3.14,
                    value="value_example",
                ),
            },
            ids=MetaIdsQuery(
                values=[
                    "values_example",
                ],
            ),
            match={
                "key": MetaMatchQuery(
                    analyzer="analyzer_example",
                    boost=3.14,
                    fuzziness={},
                    operator="operator_example",
                    prefix_length=3.14,
                    query="query_example",
                ),
            },
            match_all={},
            match_bool_prefix={
                "key": MetaMatchBoolPrefixQuery(
                    analyzer="analyzer_example",
                    boost=3.14,
                    query="query_example",
                ),
            },
            match_none={},
            match_phrase={
                "key": MetaMatchPhraseQuery(
                    analyzer="analyzer_example",
                    boost=3.14,
                    query="query_example",
                ),
            },
            match_phrase_prefix={
                "key": MetaMatchPhrasePrefixQuery(
                    analyzer="analyzer_example",
                    boost=3.14,
                    query="query_example",
                ),
            },
            multi_match=MetaMultiMatchQuery(
                analyzer="analyzer_example",
                boost=3.14,
                fields=[
                    "fields_example",
                ],
                minimum_should_match=3.14,
                operator="operator_example",
                query="query_example",
                type="type_example",
            ),
            prefix={
                "key": MetaPrefixQuery(
                    boost=3.14,
                    value="value_example",
                ),
            },
            query_string=MetaQueryStringQuery(
                analyzer="analyzer_example",
                boost=3.14,
                default_field="default_field_example",
                default_operator="default_operator_example",
                fields=[
                    "fields_example",
                ],
                query="query_example",
            ),
            range={
                "key": MetaRangeQuery(
                    boost=3.14,
                    format="format_example",
                    gt="gt_example",
                    gte="gte_example",
                    lt="lt_example",
                    lte="lte_example",
                    time_zone="time_zone_example",
                ),
            },
            regexp={
                "key": MetaRegexpQuery(
                    boost=3.14,
                    flags="flags_example",
                    value="value_example",
                ),
            },
            simple_query_string=MetaSimpleQueryStringQuery(
                all_fields=True,
                analyzer="analyzer_example",
                boost=3.14,
                default_operator="default_operator_example",
                fields=[
                    "fields_example",
                ],
                query="query_example",
            ),
            term={
                "key": MetaTermQuery(
                    boost=3.14,
                    case_insensitive=True,
                    value="value_example",
                ),
            },
            terms={
                "key": {},
            },
            wildcard={
                "key": MetaWildcardQuery(
                    boost=3.14,
                    value="value_example",
                ),
            },
        ),
        size=1,
        sort=[
            "sort_example",
        ],
        timeout=1,
        track_total_hits=True,
    ) # MetaZincQuery | Query

    # example passing only required values which don't have defaults set
    try:
        # Search V2 DSL for compatible ES
        api_response = api_instance.search(index, query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Search->search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **query** | [**MetaZincQuery**](MetaZincQuery.md)| Query |

### Return type

[**MetaSearchResponse**](MetaSearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v1**
> V1SearchResponse search_v1(index, query)

Search V1

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import search
from zincsearch_sdk.model.v1_zinc_query import V1ZincQuery
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from zincsearch_sdk.model.v1_search_response import V1SearchResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4080
# See configuration.py for a list of all supported configuration parameters.
configuration = zincsearch_sdk.Configuration(
    host = "http://localhost:4080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = zincsearch_sdk.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with zincsearch_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = search.Search(api_client)
    index = "index_example" # str | Index
    query = V1ZincQuery(
        source=[
            "source_example",
        ],
        aggs={
            "key": V1AggregationParams(
                agg_type="agg_type_example",
                aggs={},
                date_ranges=[
                    V1AggregationDateRange(
                        _from="_from_example",
                        to="to_example",
                    ),
                ],
                field="field_example",
                ranges=[
                    V1AggregationNumberRange(
                        _from=3.14,
                        to=3.14,
                    ),
                ],
                size=1,
                weight_field="weight_field_example",
            ),
        },
        explain=True,
        _from=1,
        highlight=V1QueryHighlight(
            fields=[
                "fields_example",
            ],
            style="style_example",
        ),
        max_results=1,
        query=V1QueryParams(
            boost=1,
            end_time="end_time_example",
            field="field_example",
            start_time="start_time_example",
            term="term_example",
            terms=[
                [
                    "string_example",
                ],
            ],
        ),
        search_type="search_type_example",
        sort_fields=[
            "sort_fields_example",
        ],
    ) # V1ZincQuery | Query

    # example passing only required values which don't have defaults set
    try:
        # Search V1
        api_response = api_instance.search_v1(index, query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Search->search_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **query** | [**V1ZincQuery**](V1ZincQuery.md)| Query |

### Return type

[**V1SearchResponse**](V1SearchResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

