# FlatPunchResults.Item Property

Parent Object: [FlatPunchResults](../FlatPunchResults/FlatPunchResults.md)

## Description

Returns the specified FlatPunchResult object from the collection

## Syntax

FlatPunchResults.**Item**( ***Index*** As Variant ) As [FlatPunchResult](../FlatPunchResult/FlatPunchResult.md)

## Property Value

This is a read only property whose value is a [FlatPunchResult](../FlatPunchResult/FlatPunchResult.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FlatPunchResult to return. This can be a numeric value indicating the index of the item in the collection, an Edge or a Face object that belongs to the resulting punch or it can be a string indicating the InternalName of the punch. If an out of range index is provided or the InternalName of a non-existing punch is provided, an error will occur. |

## Version

Introduced in version 2008
