# zincsearch_sdk.Document

All URIs are relative to *http://localhost:4080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk**](Document.md#bulk) | **POST** /api/_bulk | Bulk documents
[**delete**](Document.md#delete) | **DELETE** /api/{index}/_doc/{id} | Delete document
[**es_bulk**](Document.md#es_bulk) | **POST** /es/_bulk | ES bulk documents
[**index**](Document.md#index) | **POST** /api/{index}/_doc | Create or update document
[**index_with_id**](Document.md#index_with_id) | **PUT** /api/{index}/_doc/{id} | Create or update document with id
[**update**](Document.md#update) | **POST** /api/{index}/_update/{id} | Update document with id


# **bulk**
> MetaHTTPResponseRecordCount bulk(query)

Bulk documents

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_record_count import MetaHTTPResponseRecordCount
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
    api_instance = document.Document(api_client)
    query = "query_example" # str | Query

    # example passing only required values which don't have defaults set
    try:
        # Bulk documents
        api_response = api_instance.bulk(query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

### Return type

[**MetaHTTPResponseRecordCount**](MetaHTTPResponseRecordCount.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> MetaHTTPResponseDocument delete(index, id)

Delete document

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_document import MetaHTTPResponseDocument
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
    api_instance = document.Document(api_client)
    index = "index_example" # str | Index
    id = "id_example" # str | ID

    # example passing only required values which don't have defaults set
    try:
        # Delete document
        api_response = api_instance.delete(index, id)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **id** | **str**| ID |

### Return type

[**MetaHTTPResponseDocument**](MetaHTTPResponseDocument.md)

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

# **es_bulk**
> bool, date, datetime, dict, float, int, list, str, none_type es_bulk(query)

ES bulk documents

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
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
    api_instance = document.Document(api_client)
    query = "query_example" # str | Query

    # example passing only required values which don't have defaults set
    try:
        # ES bulk documents
        api_response = api_instance.es_bulk(query)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->es_bulk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Query |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index**
> MetaHTTPResponseID index(index, document)

Create or update document

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
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
    api_instance = document.Document(api_client)
    index = "index_example" # str | Index
    document = {} # bool, date, datetime, dict, float, int, list, str, none_type | Document

    # example passing only required values which don't have defaults set
    try:
        # Create or update document
        api_response = api_instance.index(index, document)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->index: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **document** | **bool, date, datetime, dict, float, int, list, str, none_type**| Document |

### Return type

[**MetaHTTPResponseID**](MetaHTTPResponseID.md)

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

# **index_with_id**
> MetaHTTPResponseID index_with_id(index, id, document)

Create or update document with id

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
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
    api_instance = document.Document(api_client)
    index = "index_example" # str | Index
    id = "id_example" # str | ID
    document = {} # bool, date, datetime, dict, float, int, list, str, none_type | Document

    # example passing only required values which don't have defaults set
    try:
        # Create or update document with id
        api_response = api_instance.index_with_id(index, id, document)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->index_with_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **id** | **str**| ID |
 **document** | **bool, date, datetime, dict, float, int, list, str, none_type**| Document |

### Return type

[**MetaHTTPResponseID**](MetaHTTPResponseID.md)

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

# **update**
> MetaHTTPResponseID update(index, id, document)

Update document with id

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
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
    api_instance = document.Document(api_client)
    index = "index_example" # str | Index
    id = "id_example" # str | ID
    document = {} # bool, date, datetime, dict, float, int, list, str, none_type | Document

    # example passing only required values which don't have defaults set
    try:
        # Update document with id
        api_response = api_instance.update(index, id, document)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **str**| Index |
 **id** | **str**| ID |
 **document** | **bool, date, datetime, dict, float, int, list, str, none_type**| Document |

### Return type

[**MetaHTTPResponseID**](MetaHTTPResponseID.md)

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

