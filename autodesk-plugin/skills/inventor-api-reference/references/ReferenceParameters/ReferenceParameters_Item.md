# ReferenceParameters.Item Property

Parent Object: [ReferenceParameters](../ReferenceParameters/ReferenceParameters.md)

## Description

Returns the specified ReferenceParameter object from the collection. This is the default property of the ReferenceParameters collection object.

## Syntax

ReferenceParameters.**Item**( ***Index*** As Variant ) As [ReferenceParameter](../ReferenceParameter/ReferenceParameter.md)

## Property Value

This is a read only property whose value is a [ReferenceParameter](../ReferenceParameter/ReferenceParameter.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the ReferenceParameter to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the parameter name. If an out of range index or a name of a non-existent parameter is provided, an error occurs. |

## Version

Introduced in version 4
