# PropertySets.Add Method

Parent Object: [PropertySets](../PropertySets/PropertySets.md)

## Description

Adds a new PropertySet. The new set's FMTID can be optionally provided (as a string).

## Syntax

PropertySets.**Add**( ***Name*** As String, [***InternalName***] As Variant ) As [PropertySet](../PropertySet/PropertySet.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Name of the PropertySet. If the name begins with an underscore the property set is hidden and can only be retrieved by asking for it by name. |
| InternalName | Variant | Input Variant that specifies the internal name of the PropertySet to be added. |

## Version

Introduced in version 4
