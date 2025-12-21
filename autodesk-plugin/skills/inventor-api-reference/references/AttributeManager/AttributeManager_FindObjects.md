# AttributeManager.FindObjects Method

Parent Object: [AttributeManager](../AttributeManager/AttributeManager.md)

## Description

Method that returns the objects that have the specified attributes.

## Remarks

**About performance** Using this method improves the performance of subsequent attributes queries. Calling this method populates certain internal caches. Thus the time required to query attributeSets properties on these objects is dramatically reduced. These caches remain valid till you change or close the document(s). This affects only the objects owned by the document. To use this method just for the purpose of populating the cache, you should call it without any arguments.

## Syntax

AttributeManager.**FindObjects**( [***AttributeSetName***] As String, [***AttributeName***] As String, [***AttributeValue***] As Variant ) As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeSetName | String | Optional input String value that specifies the name of the attribute set. An asterisk can be used as a wild card in the string to match partial strings. If this value is not input it will default to "\*" which will match all attribute sets. The search is not case sensitive. |
| AttributeName | String | Optional input String value that specifies the name of the attribute. An asterisk can be used as a wild card in the string to match partial strings. If this value is not input it will default to "\*" which will match all attributes. The search is not case sensitive.   This is an optional argument whose default value is "\*". |
| AttributeValue | Variant | Optional input Variant value that specifies the value of the attribute. In the case of attributes that contain string values, an asterisk can be used as a wild card in the string to match partial strings. For other types, exact matches must be made. For some types, the value will be ignored, i.e. arrays. If this argument is not specified it will ignore the value and match based on the AttributeSetName and AttributeName arguments.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5
