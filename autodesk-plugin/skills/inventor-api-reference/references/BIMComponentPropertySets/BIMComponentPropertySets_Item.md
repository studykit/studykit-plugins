# BIMComponentPropertySets.Item Property

Parent Object: [BIMComponentPropertySets](../BIMComponentPropertySets/BIMComponentPropertySets.md)

## Description

Returns the specified BIMComponentPropertySet object from the collection. This collection is empty until the component type is defined using the ComponentType property of the BIMComponentDescription object.

## Syntax

BIMComponentPropertySets.**Item**( ***Index*** As Variant ) As [BIMComponentPropertySet](../BIMComponentPropertySet/BIMComponentPropertySet.md)

## Property Value

This is a read only property whose value is a [BIMComponentPropertySet](../BIMComponentPropertySet/BIMComponentPropertySet.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the BIM component property set to return. This is the index of the item in the collection where the first item is 1. It can also be the name or internal name of the property set. If an out of range value or an unknown name is provided an error will occur. |

## Version

Introduced in version 2011
