"""
    Zinc Search engine API

    Zinc Search engine API documents https://docs.zincsearch.com  # noqa: E501

    The version of the OpenAPI document: 0.3.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import zincsearch_sdk
from zincsearch_sdk.model.meta_bool_query import MetaBoolQuery
from zincsearch_sdk.model.meta_exists_query import MetaExistsQuery
from zincsearch_sdk.model.meta_fuzzy_query import MetaFuzzyQuery
from zincsearch_sdk.model.meta_ids_query import MetaIdsQuery
from zincsearch_sdk.model.meta_match_bool_prefix_query import MetaMatchBoolPrefixQuery
from zincsearch_sdk.model.meta_match_phrase_prefix_query import MetaMatchPhrasePrefixQuery
from zincsearch_sdk.model.meta_match_phrase_query import MetaMatchPhraseQuery
from zincsearch_sdk.model.meta_match_query import MetaMatchQuery
from zincsearch_sdk.model.meta_multi_match_query import MetaMultiMatchQuery
from zincsearch_sdk.model.meta_prefix_query import MetaPrefixQuery
from zincsearch_sdk.model.meta_query_string_query import MetaQueryStringQuery
from zincsearch_sdk.model.meta_range_query import MetaRangeQuery
from zincsearch_sdk.model.meta_regexp_query import MetaRegexpQuery
from zincsearch_sdk.model.meta_simple_query_string_query import MetaSimpleQueryStringQuery
from zincsearch_sdk.model.meta_term_query import MetaTermQuery
from zincsearch_sdk.model.meta_wildcard_query import MetaWildcardQuery
globals()['MetaBoolQuery'] = MetaBoolQuery
globals()['MetaExistsQuery'] = MetaExistsQuery
globals()['MetaFuzzyQuery'] = MetaFuzzyQuery
globals()['MetaIdsQuery'] = MetaIdsQuery
globals()['MetaMatchBoolPrefixQuery'] = MetaMatchBoolPrefixQuery
globals()['MetaMatchPhrasePrefixQuery'] = MetaMatchPhrasePrefixQuery
globals()['MetaMatchPhraseQuery'] = MetaMatchPhraseQuery
globals()['MetaMatchQuery'] = MetaMatchQuery
globals()['MetaMultiMatchQuery'] = MetaMultiMatchQuery
globals()['MetaPrefixQuery'] = MetaPrefixQuery
globals()['MetaQueryStringQuery'] = MetaQueryStringQuery
globals()['MetaRangeQuery'] = MetaRangeQuery
globals()['MetaRegexpQuery'] = MetaRegexpQuery
globals()['MetaSimpleQueryStringQuery'] = MetaSimpleQueryStringQuery
globals()['MetaTermQuery'] = MetaTermQuery
globals()['MetaWildcardQuery'] = MetaWildcardQuery
from zincsearch_sdk.model.meta_query import MetaQuery


class TestMetaQuery(unittest.TestCase):
    """MetaQuery unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMetaQuery(self):
        """Test MetaQuery"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MetaQuery()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
