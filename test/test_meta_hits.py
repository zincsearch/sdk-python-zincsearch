"""
    Zinc Search engine API

    Zinc Search engine API documents https://docs.zincsearch.com  # noqa: E501

    The version of the OpenAPI document: 0.2.4
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import zincsearch_sdk
from zincsearch_sdk.model.meta_hit import MetaHit
from zincsearch_sdk.model.meta_total import MetaTotal
globals()['MetaHit'] = MetaHit
globals()['MetaTotal'] = MetaTotal
from zincsearch_sdk.model.meta_hits import MetaHits


class TestMetaHits(unittest.TestCase):
    """MetaHits unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetaHits(self):
        """Test MetaHits"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetaHits()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
