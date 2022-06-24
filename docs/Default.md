# zincsearch_sdk.Default

All URIs are relative to *http://localhost:4080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz**](Default.md#healthz) | **GET** /healthz | Get healthz
[**version**](Default.md#version) | **GET** /version | Get version


# **healthz**
> MetaHealthzResponse healthz()

Get healthz

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import default
from zincsearch_sdk.model.meta_healthz_response import MetaHealthzResponse
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
    api_instance = default.Default(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get healthz
        api_response = api_instance.healthz()
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Default->healthz: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MetaHealthzResponse**](MetaHealthzResponse.md)

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

# **version**
> MetaVersionResponse version()

Get version

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import default
from zincsearch_sdk.model.meta_version_response import MetaVersionResponse
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
    api_instance = default.Default(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get version
        api_response = api_instance.version()
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Default->version: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MetaVersionResponse**](MetaVersionResponse.md)

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

