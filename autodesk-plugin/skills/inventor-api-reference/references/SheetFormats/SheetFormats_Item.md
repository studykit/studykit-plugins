# SheetFormats.Item Property

Parent Object: [SheetFormats](../SheetFormats/SheetFormats.md)

## Description

Returns the specified SheetFormat object from the collection.

## Syntax

SheetFormats.**Item**( ***Index*** As Variant ) As [SheetFormat](../SheetFormat/SheetFormat.md)

## Property Value

This is a read only property whose value is a [SheetFormat](../SheetFormat/SheetFormat.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Index | Variant | Input Variant value that specifies the SheetFormat to return. This can be either a numeric value indicating the index of the item in the collection or it can be a string indicating the SheetFormat name. If an out of range index or a name of a non-existent SheetFormat is provided, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet with multiple views](../../sample-programs/SheetFormat_Sample.md) | This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views. |

## Version

Introduced in version 2009
