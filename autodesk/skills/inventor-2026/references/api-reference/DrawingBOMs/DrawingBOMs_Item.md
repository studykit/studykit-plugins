# DrawingBOMs.Item Property

Parent Object: [DrawingBOMs](../DrawingBOMs/DrawingBOMs.md)

## Description

Returns the specified DrawingBOM object from the collection.

## Syntax

DrawingBOMs.**Item**( ***Index*** As Variant ) As [DrawingBOM](../DrawingBOM/DrawingBOM.md)

## Property Value

This is a read only property whose value is a [DrawingBOM](../DrawingBOM/DrawingBOM.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DrawingBOM to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the FullFileName of the model document referenced by the DrawingBOM. If the input is an out of range index or the file name of a model for which a DrawingBOM has not yet been created, an error will occur. |

## Version

Introduced in version 2009
