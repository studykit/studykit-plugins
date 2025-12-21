# AttributeSets.Item Property

Parent Object: [AttributeSets](../AttributeSets/AttributeSets.md)

## Description

Returns the specified object from the collection. This is the default property of the AttributeSets collection object.

## Syntax

AttributeSets.**Item**( ***Index*** As Variant ) As [AttributeSet](../AttributeSet/AttributeSet.md)

## Property Value

This is a read only property whose value is an [AttributeSet](../AttributeSet/AttributeSet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the attribute set name. If an out-of-range index or a name of a nonexistent attribute set is provided, an error occurs. |

## Version

Introduced in version 5
