# zincsearch_sdk.Index

All URIs are relative to *http://localhost:4080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analyze**](Index.md#analyze) | **POST** /api/_analyze | Analyze
[**analyze_index**](Index.md#analyze_index) | **POST** /api/{index}/_analyze | Analyze
[**create**](Index.md#create) | **POST** /api/index | Create index
[**create_template**](Index.md#create_template) | **POST** /es/_index_template | Create update index template
[**delete**](Index.md#delete) | **DELETE** /api/index/{index} | Delete index
[**delete_template**](Index.md#delete_template) | **DELETE** /es/_index_template/{name} | Delete template
[**e_s_create_index**](Index.md#e_s_create_index) | **PUT** /es/{index} | Create index for compatible ES
[**e_s_get_mapping**](Index.md#e_s_get_mapping) | **GET** /es/{index}/_mapping | Get index mappings for compatible ES
[**es_exists**](Index.md#es_exists) | **HEAD** /es/{index} | Checks if the index exists for compatible ES
[**exists**](Index.md#exists) | **HEAD** /api/index/{index} | Checks if the index exists
[**get_mapping**](Index.md#get_mapping) | **GET** /api/{index}/_mapping | Get index mappings
[**get_settings**](Index.md#get_settings) | **GET** /api/{index}/_settings | Get index settings
[**get_template**](Index.md#get_template) | **GET** /es/_index_template/{name} | Get index template
[**index_name_list**](Index.md#index_name_list) | **GET** /api/index_name | List index Name
[**list**](Index.md#list) | **GET** /api/index | List indexes
[**list_templates**](Index.md#list_templates) | **GET** /es/_index_template | List index teplates
[**refresh**](Index.md#refresh) | **POST** /api/index/{index}/refresh | Resfresh index
[**set_mapping**](Index.md#set_mapping) | **PUT** /api/{index}/_mapping | Set index mappings
[**set_settings**](Index.md#set_settings) | **PUT** /api/{index}/_settings | Set index Settings
[**update_template**](Index.md#update_template) | **PUT** /es/_index_template/{name} | Create update index template


# **analyze**
> IndexAnalyzeResponse analyze(query)

Analyze

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.index_analyze_response import IndexAnalyzeResponse
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
    api_instance = index.Index(api_client)
    query = {} # bool, date, datetime, dict, float, int, list, str, none_type | Query

    # example passing only required values which don't have defaults set
    try:
        # Analyze
        api_response = api_instance.analyze(query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->analyze: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **bool, date, datetime, dict, float, int, list, str, none_type**| Query |

### Return type

[**IndexAnalyzeResponse**](IndexAnalyzeResponse.md)

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

# **analyze_index**
> IndexAnalyzeResponse analyze_index(index, query)

Analyze

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.index_analyze_response import IndexAnalyzeResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index
    query = {} # bool, date, datetime, dict, float, int, list, str, none_type | Query

    # example passing only required values which don't have defaults set
    try:
        # Analyze
        api_response = api_instance.analyze_index(index, query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->analyze_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **query** | **bool, date, datetime, dict, float, int, list, str, none_type**| Query |

### Return type

[**IndexAnalyzeResponse**](IndexAnalyzeResponse.md)

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

# **create**
> MetaHTTPResponseIndex create(data)

Create index

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response_index import MetaHTTPResponseIndex
from zincsearch_sdk.model.meta_index_simple import MetaIndexSimple
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
    api_instance = index.Index(api_client)
    data = MetaIndexSimple(
        mappings={},
        name="name_example",
        settings=MetaIndexSettings(
            analysis=MetaIndexAnalysis(
                analyzer={
                    "key": MetaAnalyzer(
                        char_filter=[
                            "char_filter_example",
                        ],
                        filter=[
                            "filter_example",
                        ],
                        lowercase=True,
                        pattern="pattern_example",
                        stopwords=[
                            "stopwords_example",
                        ],
                        token_filter=[
                            "token_filter_example",
                        ],
                        tokenizer="tokenizer_example",
                        type="type_example",
                    ),
                },
                char_filter={},
                filter={},
                token_filter={},
                tokenizer={},
            ),
            number_of_replicas=1,
            number_of_shards=1,
        ),
        shard_num=1,
        storage_type="storage_type_example",
    ) # MetaIndexSimple | Index data

    # example passing only required values which don't have defaults set
    try:
        # Create index
        api_response = api_instance.create(data)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MetaIndexSimple**](MetaIndexSimple.md)| Index data |

### Return type

[**MetaHTTPResponseIndex**](MetaHTTPResponseIndex.md)

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

# **create_template**
> MetaHTTPResponseTemplate create_template(template)

Create update index template

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_index_template import MetaIndexTemplate
from zincsearch_sdk.model.meta_http_response_template import MetaHTTPResponseTemplate
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
    api_instance = index.Index(api_client)
    template = MetaIndexTemplate(
        created_at="created_at_example",
        index_patterns=[
            "index_patterns_example",
        ],
        priority=1,
        template=MetaTemplateTemplate(
            mappings=MetaMappings(
                properties={
                    "key": MetaProperty(
                        aggregatable=True,
                        analyzer="analyzer_example",
                        fields={
                            "key": MetaProperty(),
                        },
                        format="format_example",
                        highlightable=True,
                        index=True,
                        search_analyzer="search_analyzer_example",
                        sortable=True,
                        store=True,
                        time_zone="time_zone_example",
                        type="type_example",
                    ),
                },
            ),
            settings=MetaIndexSettings(
                analysis=MetaIndexAnalysis(
                    analyzer={
                        "key": MetaAnalyzer(
                            char_filter=[
                                "char_filter_example",
                            ],
                            filter=[
                                "filter_example",
                            ],
                            lowercase=True,
                            pattern="pattern_example",
                            stopwords=[
                                "stopwords_example",
                            ],
                            token_filter=[
                                "token_filter_example",
                            ],
                            tokenizer="tokenizer_example",
                            type="type_example",
                        ),
                    },
                    char_filter={},
                    filter={},
                    token_filter={},
                    tokenizer={},
                ),
                number_of_replicas=1,
                number_of_shards=1,
            ),
        ),
        updated_at="updated_at_example",
    ) # MetaIndexTemplate | Template data

    # example passing only required values which don't have defaults set
    try:
        # Create update index template
        api_response = api_instance.create_template(template)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->create_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template** | [**MetaIndexTemplate**](MetaIndexTemplate.md)| Template data |

### Return type

[**MetaHTTPResponseTemplate**](MetaHTTPResponseTemplate.md)

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

# **delete**
> MetaHTTPResponseIndex delete(index)

Delete index

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response_index import MetaHTTPResponseIndex
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Delete index
        api_response = api_instance.delete(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

[**MetaHTTPResponseIndex**](MetaHTTPResponseIndex.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> MetaHTTPResponse delete_template(name)

Delete template

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    name = "name_example" # str | Template

    # example passing only required values which don't have defaults set
    try:
        # Delete template
        api_response = api_instance.delete_template(name)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->delete_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **e_s_create_index**
> bool, date, datetime, dict, float, int, list, str, none_type e_s_create_index(index, data)

Create index for compatible ES

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
from zincsearch_sdk.model.meta_index_simple import MetaIndexSimple
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index
    data = MetaIndexSimple(
        mappings={},
        name="name_example",
        settings=MetaIndexSettings(
            analysis=MetaIndexAnalysis(
                analyzer={
                    "key": MetaAnalyzer(
                        char_filter=[
                            "char_filter_example",
                        ],
                        filter=[
                            "filter_example",
                        ],
                        lowercase=True,
                        pattern="pattern_example",
                        stopwords=[
                            "stopwords_example",
                        ],
                        token_filter=[
                            "token_filter_example",
                        ],
                        tokenizer="tokenizer_example",
                        type="type_example",
                    ),
                },
                char_filter={},
                filter={},
                token_filter={},
                tokenizer={},
            ),
            number_of_replicas=1,
            number_of_shards=1,
        ),
        shard_num=1,
        storage_type="storage_type_example",
    ) # MetaIndexSimple | Index data

    # example passing only required values which don't have defaults set
    try:
        # Create index for compatible ES
        api_response = api_instance.e_s_create_index(index, data)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->e_s_create_index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **data** | [**MetaIndexSimple**](MetaIndexSimple.md)| Index data |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **e_s_get_mapping**
> bool, date, datetime, dict, float, int, list, str, none_type e_s_get_mapping(index)

Get index mappings for compatible ES

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Get index mappings for compatible ES
        api_response = api_instance.e_s_get_mapping(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->e_s_get_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **es_exists**
> MetaHTTPResponse es_exists(index)

Checks if the index exists for compatible ES

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Checks if the index exists for compatible ES
        api_response = api_instance.es_exists(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->es_exists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exists**
> MetaHTTPResponse exists(index)

Checks if the index exists

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Checks if the index exists
        api_response = api_instance.exists(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->exists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> bool, date, datetime, dict, float, int, list, str, none_type get_mapping(index)

Get index mappings

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Get index mappings
        api_response = api_instance.get_mapping(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->get_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings**
> bool, date, datetime, dict, float, int, list, str, none_type get_settings(index)

Get index settings

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Get index settings
        api_response = api_instance.get_settings(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->get_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MetaIndexTemplate get_template(name)

Get index template

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_index_template import MetaIndexTemplate
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
    api_instance = index.Index(api_client)
    name = "name_example" # str | Template

    # example passing only required values which don't have defaults set
    try:
        # Get index template
        api_response = api_instance.get_template(name)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->get_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template |

### Return type

[**MetaIndexTemplate**](MetaIndexTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_name_list**
> [str] index_name_list()

List index Name

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
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
    api_instance = index.Index(api_client)
    name = "name_example" # str | IndexName (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List index Name
        api_response = api_instance.index_name_list(name=name)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->index_name_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| IndexName | [optional]

### Return type

**[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> IndexIndexListResponse list()

List indexes

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.index_index_list_response import IndexIndexListResponse
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
    api_instance = index.Index(api_client)
    page_num = 1 # int | page num (optional)
    page_size = 1 # int | page size (optional)
    sort_by = "sort_by_example" # str | sort by (optional)
    desc = True # bool | desc (optional)
    name = "name_example" # str | name (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List indexes
        api_response = api_instance.list(page_num=page_num, page_size=page_size, sort_by=sort_by, desc=desc, name=name)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_num** | **int**| page num | [optional]
 **page_size** | **int**| page size | [optional]
 **sort_by** | **str**| sort by | [optional]
 **desc** | **bool**| desc | [optional]
 **name** | **str**| name | [optional]

### Return type

[**IndexIndexListResponse**](IndexIndexListResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> [MetaTemplate] list_templates()

List index teplates

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from zincsearch_sdk.model.meta_template import MetaTemplate
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
    api_instance = index.Index(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List index teplates
        api_response = api_instance.list_templates()
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->list_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[MetaTemplate]**](MetaTemplate.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> MetaHTTPResponse refresh(index)

Resfresh index

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index

    # example passing only required values which don't have defaults set
    try:
        # Resfresh index
        api_response = api_instance.refresh(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->refresh: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mapping**
> MetaHTTPResponse set_mapping(index, mapping)

Set index mappings

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
from zincsearch_sdk.model.meta_mappings import MetaMappings
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index
    mapping = MetaMappings(
        properties={
            "key": MetaProperty(
                aggregatable=True,
                analyzer="analyzer_example",
                fields={
                    "key": MetaProperty(),
                },
                format="format_example",
                highlightable=True,
                index=True,
                search_analyzer="search_analyzer_example",
                sortable=True,
                store=True,
                time_zone="time_zone_example",
                type="type_example",
            ),
        },
    ) # MetaMappings | Mapping

    # example passing only required values which don't have defaults set
    try:
        # Set index mappings
        api_response = api_instance.set_mapping(index, mapping)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->set_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **mapping** | [**MetaMappings**](MetaMappings.md)| Mapping |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_settings**
> MetaHTTPResponse set_settings(index, settings)

Set index Settings

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_index_settings import MetaIndexSettings
from zincsearch_sdk.model.meta_http_response import MetaHTTPResponse
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
    api_instance = index.Index(api_client)
    index = "index_example" # str | Index
    settings = MetaIndexSettings(
        analysis=MetaIndexAnalysis(
            analyzer={
                "key": MetaAnalyzer(
                    char_filter=[
                        "char_filter_example",
                    ],
                    filter=[
                        "filter_example",
                    ],
                    lowercase=True,
                    pattern="pattern_example",
                    stopwords=[
                        "stopwords_example",
                    ],
                    token_filter=[
                        "token_filter_example",
                    ],
                    tokenizer="tokenizer_example",
                    type="type_example",
                ),
            },
            char_filter={},
            filter={},
            token_filter={},
            tokenizer={},
        ),
        number_of_replicas=1,
        number_of_shards=1,
    ) # MetaIndexSettings | Settings

    # example passing only required values which don't have defaults set
    try:
        # Set index Settings
        api_response = api_instance.set_settings(index, settings)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->set_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **settings** | [**MetaIndexSettings**](MetaIndexSettings.md)| Settings |

### Return type

[**MetaHTTPResponse**](MetaHTTPResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> MetaHTTPResponseTemplate update_template(name, template)

Create update index template

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_index_template import MetaIndexTemplate
from zincsearch_sdk.model.meta_http_response_template import MetaHTTPResponseTemplate
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
    api_instance = index.Index(api_client)
    name = "name_example" # str | Template
    template = MetaIndexTemplate(
        created_at="created_at_example",
        index_patterns=[
            "index_patterns_example",
        ],
        priority=1,
        template=MetaTemplateTemplate(
            mappings=MetaMappings(
                properties={
                    "key": MetaProperty(
                        aggregatable=True,
                        analyzer="analyzer_example",
                        fields={
                            "key": MetaProperty(),
                        },
                        format="format_example",
                        highlightable=True,
                        index=True,
                        search_analyzer="search_analyzer_example",
                        sortable=True,
                        store=True,
                        time_zone="time_zone_example",
                        type="type_example",
                    ),
                },
            ),
            settings=MetaIndexSettings(
                analysis=MetaIndexAnalysis(
                    analyzer={
                        "key": MetaAnalyzer(
                            char_filter=[
                                "char_filter_example",
                            ],
                            filter=[
                                "filter_example",
                            ],
                            lowercase=True,
                            pattern="pattern_example",
                            stopwords=[
                                "stopwords_example",
                            ],
                            token_filter=[
                                "token_filter_example",
                            ],
                            tokenizer="tokenizer_example",
                            type="type_example",
                        ),
                    },
                    char_filter={},
                    filter={},
                    token_filter={},
                    tokenizer={},
                ),
                number_of_replicas=1,
                number_of_shards=1,
            ),
        ),
        updated_at="updated_at_example",
    ) # MetaIndexTemplate | Template data

    # example passing only required values which don't have defaults set
    try:
        # Create update index template
        api_response = api_instance.update_template(name, template)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->update_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Template |
 **template** | [**MetaIndexTemplate**](MetaIndexTemplate.md)| Template data |

### Return type

[**MetaHTTPResponseTemplate**](MetaHTTPResponseTemplate.md)

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

