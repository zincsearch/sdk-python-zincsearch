"""
* Copyright 2022 Zinc Labs Inc. and Contributors
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
"""

import time
import zincsearch_sdk
from zincsearch_sdk.api import document
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
from zincsearch_sdk.model.meta_http_response_id import MetaHTTPResponseID
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = zincsearch_sdk.Configuration(
    host = "http://localhost:4080",
    username = 'admin',
    password = 'Complexpass#123'
)

# Enter a context with an instance of the API client
with zincsearch_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = document.Document(api_client)
    index = "index_example" # str | Index
    document = {
        "name": "John Doe",
        "age": 30,
        "address": "123 Main St"
    } # bool, date, datetime, dict, float, int, list, str, none_type | Document

    # example passing only required values which don't have defaults set
    try:
        # Create or update document
        api_response = api_instance.index(index, document)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Document->index: %s\n" % e)
