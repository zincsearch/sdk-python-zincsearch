# MetaZincQuery


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **[str]** | true, false, [\&quot;field1\&quot;, \&quot;field2.*\&quot;] | [optional] 
**aggs** | [**{str: (MetaAggregations,)}**](MetaAggregations.md) |  | [optional] 
**explain** | **bool** |  | [optional] 
**fields** | **[str]** | [\&quot;field1\&quot;, \&quot;field2.*\&quot;, {\&quot;field\&quot;: \&quot;fieldName\&quot;, \&quot;format\&quot;: \&quot;epoch_millis\&quot;}] | [optional] 
**_from** | **int** |  | [optional] 
**highlight** | [**MetaHighlight**](MetaHighlight.md) |  | [optional] 
**query** | [**MetaQuery**](MetaQuery.md) |  | [optional] 
**size** | **int** |  | [optional] 
**sort** | **[str]** | \&quot;_sorce\&quot;, [\&quot;+Year\&quot;,\&quot;-Year\&quot;, {\&quot;Year\&quot;: \&quot;desc\&quot;}, \&quot;Date\&quot;: {\&quot;order\&quot;: \&quot;asc\&quot;\&quot;, \&quot;format\&quot;: \&quot;yyyy-MM-dd\&quot;}}\&quot;}] | [optional] 
**timeout** | **int** |  | [optional] 
**track_total_hits** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


