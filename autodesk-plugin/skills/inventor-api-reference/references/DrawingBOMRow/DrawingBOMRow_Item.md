# DrawingBOMRow.Item Property

Parent Object: [DrawingBOMRow](../DrawingBOMRow/DrawingBOMRow.md)

## Description

## Syntax

DrawingBOMRow.**Item**( ***Index*** As Variant ) As [DrawingBOMCell](../DrawingBOMCell/DrawingBOMCell.md)

## Property Value

This is a read only property whose value is a [DrawingBOMCell](../DrawingBOMCell/DrawingBOMCell.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the DrawingBOMCell to return. This can be either a numeric value indicating the index of the item in the collection, a string indicating the title of a column, or a DrawingBOMColumn object. If an out of range index, a non-existent column title, or an invalid DrawingBOMColumn object is specified, an error occurs. |

## Version

Introduced in version 2009
