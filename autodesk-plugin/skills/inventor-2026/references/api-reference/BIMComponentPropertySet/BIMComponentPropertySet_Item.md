# BIMComponentPropertySet.Item Property

Parent Object: [BIMComponentPropertySet](../BIMComponentPropertySet/BIMComponentPropertySet.md)

## Description

Returns the specified BIMComponentProperty object from the collection.

## Syntax

BIMComponentPropertySet.**Item**( ***Index*** As Variant ) As [BIMComponentProperty](../BIMComponentProperty/BIMComponentProperty.md)

## Property Value

This is a read only property whose value is a [BIMComponentProperty](../BIMComponentProperty/BIMComponentProperty.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BIM component property to return. This is the index of the item in the collection where the first item is 1. It can also be the name or internal name of the property. If an out of range value or an unknown name is provided an error will occur. |

## Version

Introduced in version 2011
