# AutoCADBlockDefinition.CopyTo Method

Parent Object: [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md)

## Description

Method that copies the definition to the target drawing document.

## Syntax

AutoCADBlockDefinition.**CopyTo**( ***TargetDocument*** As [DrawingDocument](../DrawingDocument/DrawingDocument.md), [***ReplaceExisting***] As Boolean ) As [AutoCADBlockDefinition](../AutoCADBlockDefinition/AutoCADBlockDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetDocument | [DrawingDocument](../DrawingDocument/DrawingDocument.md) | Input DrawingDocument object that specifies the document to copy the definition into. The target document must be an Inventor DWG drawing (not an IDW). |
| ReplaceExisting | Boolean | Optional input Boolean that specifies whether to replace or create a new definition with a different name if a definition of the same name exists in the target document. If not specified, the argument |

## Version

Introduced in version 2011
