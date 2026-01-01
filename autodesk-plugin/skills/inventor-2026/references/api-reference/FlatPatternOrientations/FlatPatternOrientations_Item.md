# FlatPatternOrientations.Item Property

Parent Object: [FlatPatternOrientations](../FlatPatternOrientations/FlatPatternOrientations.md)

## Description

Allows VARIANT-indexed access to items in the collection. You can use names as indexes as well.

## Syntax

FlatPatternOrientations.**Item**( ***Index*** As Variant ) As [FlatPatternOrientation](../FlatPatternOrientation/FlatPatternOrientation.md)

## Property Value

This is a read only property whose value is a [FlatPatternOrientation](../FlatPatternOrientation/FlatPatternOrientation.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the FlatPatternOrientation to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the FlatPatternOrientation name. If an out of range index or a name of a non-existent FlatPatternOrientation is provided, an error will occur. |

## Version

Introduced in version 2015
