
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from zincsearch_sdk.api.document import Document
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from zincsearch_sdk.api.document import Document
from zincsearch_sdk.api.index import Index
from zincsearch_sdk.api.search import Search
from zincsearch_sdk.api.user import User
from zincsearch_sdk.api.default import Default
