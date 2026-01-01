# AttributeSet.Item Property

Parent Object: [AttributeSet](../AttributeSet/AttributeSet.md)

## Description

Returns the specified Attribute object from the attribute set. This is the default property of the AttributeSet object.

## Syntax

AttributeSet.**Item**( ***Index*** As Variant ) As [Attribute](../Attribute/Attribute.md)

## Property Value

This is a read only property whose value is an [Attribute](../Attribute/Attribute.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the attribute name. If an out-of-range index or a name of a nonexistent attribute is provided, an error occurs. |

## Version

Introduced in version 5
