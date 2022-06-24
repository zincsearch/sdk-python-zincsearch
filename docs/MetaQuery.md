# MetaQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bool** | [**MetaBoolQuery**](MetaBoolQuery.md) |  | [optional] 
**exists** | [**MetaExistsQuery**](MetaExistsQuery.md) |  | [optional] 
**fuzzy** | [**{str: (MetaFuzzyQuery,)}**](MetaFuzzyQuery.md) | simple, PrefixQuery | [optional] 
**ids** | [**MetaIdsQuery**](MetaIdsQuery.md) |  | [optional] 
**match** | [**{str: (MetaMatchQuery,)}**](MetaMatchQuery.md) | simple, MatchQuery | [optional] 
**match_all** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**match_bool_prefix** | [**{str: (MetaMatchBoolPrefixQuery,)}**](MetaMatchBoolPrefixQuery.md) | simple, MatchBoolPrefixQuery | [optional] 
**match_none** | **bool, date, datetime, dict, float, int, list, str, none_type** |  | [optional] 
**match_phrase** | [**{str: (MetaMatchPhraseQuery,)}**](MetaMatchPhraseQuery.md) | simple, MatchPhraseQuery | [optional] 
**match_phrase_prefix** | [**{str: (MetaMatchPhrasePrefixQuery,)}**](MetaMatchPhrasePrefixQuery.md) | simple, MatchPhrasePrefixQuery | [optional] 
**multi_match** | [**MetaMultiMatchQuery**](MetaMultiMatchQuery.md) |  | [optional] 
**prefix** | [**{str: (MetaPrefixQuery,)}**](MetaPrefixQuery.md) | . | [optional] 
**query_string** | [**MetaQueryStringQuery**](MetaQueryStringQuery.md) |  | [optional] 
**range** | [**{str: (MetaRangeQuery,)}**](MetaRangeQuery.md) | simple, FuzzyQuery | [optional] 
**regexp** | [**{str: (MetaRegexpQuery,)}**](MetaRegexpQuery.md) | simple, FuzzyQuery | [optional] 
**simple_query_string** | [**MetaSimpleQueryStringQuery**](MetaSimpleQueryStringQuery.md) |  | [optional] 
**term** | [**{str: (MetaTermQuery,)}**](MetaTermQuery.md) | simple, TermQuery | [optional] 
**terms** | **{str: (dict,)}** | . | [optional] 
**wildcard** | [**{str: (MetaWildcardQuery,)}**](MetaWildcardQuery.md) | simple, WildcardQuery | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


