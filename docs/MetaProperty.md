# MetaProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregatable** | **bool** |  | [optional] 
**analyzer** | **str** |  | [optional] 
**fields** | [**{str: (MetaProperty,)}**](MetaProperty.md) | Fields allow the same string value to be indexed in multiple ways for different purposes, such as one field for search and a multi-field for sorting and aggregations, or the same string value analyzed by different analyzers. If the Fields property is defined within a sub-field, it will be ignored.  Currently, only \&quot;text\&quot; fields support the Fields parameter. | [optional] 
**format** | **str** | date format yyyy-MM-dd HH:mm:ss || yyyy-MM-dd || epoch_millis | [optional] 
**highlightable** | **bool** |  | [optional] 
**index** | **bool** |  | [optional] 
**search_analyzer** | **str** |  | [optional] 
**sortable** | **bool** |  | [optional] 
**store** | **bool** |  | [optional] 
**time_zone** | **str** | date format time_zone | [optional] 
**type** | **str** | text, keyword, date, numeric, boolean, geo_point | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


