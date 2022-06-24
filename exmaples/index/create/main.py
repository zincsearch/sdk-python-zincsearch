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
from zincsearch_sdk.api import index
from zincsearch_sdk.model.meta_http_response_index import MetaHTTPResponseIndex
from zincsearch_sdk.model.meta_index_simple import MetaIndexSimple
from zincsearch_sdk.model.meta_mappings import MetaMappings
from zincsearch_sdk.model.meta_property import MetaProperty
from zincsearch_sdk.model.meta_http_response_error import MetaHTTPResponseError
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
    api_instance = index.Index(api_client)
    index = MetaIndexSimple(
        name="index_example",
        storage_type="disk",
        mappings=MetaMappings(
            properties={
                "name": MetaProperty(
                    type="text",
                    index=True,
                    highlightable=True,
                ),
            },
        ),
    ) # MetaIndexSimple | Index data

    # example passing only required values which don't have defaults set
    try:
        # Create index
        api_response = api_instance.create(index)
        pprint(api_response)
    except zincsearch_sdk.ApiException as e:
        print("Exception when calling Index->create: %s\n" % e)
