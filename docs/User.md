# zincsearch_sdk.User

All URIs are relative to *http://localhost:4080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](User.md#create) | **POST** /api/user | Create user
[**delete**](User.md#delete) | **DELETE** /api/user/{id} | Delete user
[**list**](User.md#list) | **GET** /api/user | List user
[**login**](User.md#login) | **POST** /api/login | Login
[**update**](User.md#update) | **PUT** /api/user | Update user


# **create**
> MetaHTTPResponseID create(user)

Create user

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import user
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
from zincsearch_sdk.model.meta_user import MetaUser
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
    api_instance = user.User(api_client)
    user = MetaUser(
        id="id_example",
        created_at="created_at_example",
        name="name_example",
        password="password_example",
        role="role_example",
        salt="salt_example",
        updated_at="updated_at_example",
    ) # MetaUser | User data

    # example passing only required values which don't have defaults set
    try:
        # Create user
        api_response = api_instance.create(user)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling User->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**MetaUser**](MetaUser.md)| User data |

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

# **delete**
> MetaHTTPResponseID delete(id)

Delete user

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import user
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
    api_instance = user.User(api_client)
    id = "id_example" # str | User id

    # example passing only required values which don't have defaults set
    try:
        # Delete user
        api_response = api_instance.delete(id)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling User->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id |

### Return type

[**MetaHTTPResponseID**](MetaHTTPResponseID.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> [MetaUser] list()

List user

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import user
from zincsearch_sdk.model.meta_user import MetaUser
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
    api_instance = user.User(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List user
        api_response = api_instance.list()
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling User->list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[MetaUser]**](MetaUser.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> AuthLoginResponse login(login)

Login

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import user
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from zincsearch_sdk.model.auth_login_response import AuthLoginResponse
from zincsearch_sdk.model.auth_login_request import AuthLoginRequest
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
    api_instance = user.User(api_client)
    login = AuthLoginRequest(
        id="id_example",
        password="password_example",
    ) # AuthLoginRequest | Login credentials

    # example passing only required values which don't have defaults set
    try:
        # Login
        api_response = api_instance.login(login)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling User->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | [**AuthLoginRequest**](AuthLoginRequest.md)| Login credentials |

### Return type

[**AuthLoginResponse**](AuthLoginResponse.md)

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

# **update**
> MetaHTTPResponseID update(user)

Update user

### Example

* Basic Authentication (basicAuth):

```python
import time
import zincsearch_sdk
from zincsearch_sdk.api import user
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
from zincsearch_sdk.model.meta_user import MetaUser
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
    api_instance = user.User(api_client)
    user = MetaUser(
        id="id_example",
        created_at="created_at_example",
        name="name_example",
        password="password_example",
        role="role_example",
        salt="salt_example",
        updated_at="updated_at_example",
    ) # MetaUser | User data

    # example passing only required values which don't have defaults set
    try:
        # Update user
        api_response = api_instance.update(user)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling User->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**MetaUser**](MetaUser.md)| User data |

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

