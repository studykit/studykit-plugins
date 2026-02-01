# AttributeManager.FindAttributes Method

Parent Object: [AttributeManager](../AttributeManager/AttributeManager.md)

## Description

Method that returns the Attribute objects that match the search criteria.

## Syntax

AttributeManager.**FindAttributes**( [***AttributeSetName***] As String, [***AttributeName***] As String, [***AttributeValue***] As Variant ) As [AttributesEnumerator](../AttributesEnumerator/AttributesEnumerator.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AttributeSetName | String | Optional input String value that specifies the name of the owning attribute set. An asterisk can be used as a wild card in the string to match partial strings. If this value is not input it will default to "\*" which will match all attribute sets. The search is not case sensitive. |
| AttributeName | String | Optional input String value that specifies the name of the attribute, including a compound name that contains nested sub-Attributes. An asterisk can be used as a wild card in the string to match partial strings. A dot is used as the delimiter between an attribute and its sub-attribute. If this value is not input it will default to "\*" which will match all attributes. The search is not case sensitive. Thus, "Color.Green\*" will match an object that has an attribute whose name is "color" with a sub-attribute, "green." The sub-attribute could also be "greenish" as well and the match would succeed. But no match is found if a 'color' object is found with no sub-attributes. On the other hand, a query with simply "Color" will match all objects which may or may not have sub-attributes, but do have the direct attribute, "color."   This is an optional argument whose default value is "\*". |
| AttributeValue | Variant | Optional input Variant value that specifies the value of the attribute. In the case of attributes that contain string values, an asterisk can be used as a wild card in the string to match partial strings. For other types, exact matches must be made. For some types, the value will be ignored, i.e. arrays. If this argument is not specified it will ignore the value and match based on the AttributeSetName and AttributeName arguments.   This is an optional argument whose default value is null. |

## Version

Introduced in version 5
