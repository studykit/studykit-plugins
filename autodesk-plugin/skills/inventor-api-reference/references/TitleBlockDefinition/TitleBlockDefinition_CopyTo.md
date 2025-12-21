# TitleBlockDefinition.CopyTo Method

Parent Object: [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Description

Method that copies the definition to the target drawing document.

## Syntax

TitleBlockDefinition.**CopyTo**( ***TargetDocument*** As [DrawingDocument](../DrawingDocument/DrawingDocument.md), [***ReplaceExisting***] As Boolean ) As [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetDocument | [DrawingDocument](../DrawingDocument/DrawingDocument.md) | Input DrawingDocument object that specifies the document to copy the definition into. |
| ReplaceExisting | Boolean | Optional input Boolean that specifies whether to replace or create a new definition with a different name if a definition of the same name exists in the target document. If not specified, the argument defaults to False indicating that a new definition will be created. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 10
