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
from zincsearch_sdk.api import default
from zincsearch_sdk.model.meta_healthz_response import MetaHealthzResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:4080
# See configuration.py for a list of all supported configuration parameters.
configuration = zincsearch_sdk.Configuration(
    host = "http://localhost:4080"
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