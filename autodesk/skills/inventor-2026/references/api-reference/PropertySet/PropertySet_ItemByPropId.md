# PropertySet.ItemByPropId Property

Parent Object: [PropertySet](../PropertySet/PropertySet.md)

## Description

Gets the Property in this set by its PropId.

## Syntax

PropertySet.**ItemByPropId**( ***PropId*** As Long ) As [Property](../Property/Property.md)

## Property Value

This is a read only property whose value is a [Property](../Property/Property.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PropId | Long | Input Long that specifies the PropertyID of the Property to get from the set. Valid PropIds are 2 through 254 and 256 through 0x80000000. Other values are reserved. |

## Version

Introduced in version 4
