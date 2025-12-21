# SheetFormat.CopyTo Method

Parent Object: [SheetFormat](../SheetFormat/SheetFormat.md)

## Description

Method that copies the sheet format to the target drawing document.

## Remarks

If a sheet format of the same name exists in the target document, a new name is assigned to the copied format. Copying a sheet format also copies over the referenced titleblock definition and border definition. If definitions of the same name exist in the target document, new names are assigned to these resources as well. The method returns a failure if the target document is the same as the source document.

## Syntax

SheetFormat.**CopyTo**( ***TargetDocument*** As [DrawingDocument](../DrawingDocument/DrawingDocument.md) ) As [SheetFormat](../SheetFormat/SheetFormat.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetDocument | [DrawingDocument](../DrawingDocument/DrawingDocument.md) | Input DrawingDocument object that specifies the document to copy the format into. |

## Version

Introduced in version 2009
