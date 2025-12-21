# BorderDefinition.CopyTo Method

Parent Object: [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Description

Method that copies the definition to the target drawing document.

## Syntax

BorderDefinition.**CopyTo**( ***TargetDocument*** As [DrawingDocument](../DrawingDocument/DrawingDocument.md), [***ReplaceExisting***] As Boolean ) As [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TargetDocument | [DrawingDocument](../DrawingDocument/DrawingDocument.md) | Input DrawingDocument object that specifies the document to copy the definition into. |
| ReplaceExisting | Boolean | Optional input Boolean that specifies whether to replace or create a new definition with a different name if a definition of the same name exists in the target document. If not specified, the argument defaults to False indicating that a new definition will be created. |

## Version

Introduced in version 10
