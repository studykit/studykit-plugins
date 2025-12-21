# SketchedSymbolDefinitions.Add Method

Parent Object: [SketchedSymbolDefinitions](../SketchedSymbolDefinitions/SketchedSymbolDefinitions.md)

## Description

Method that creates a new sketched symbol definition. This method will fail in the case where a sketch is currently active. You can check for this case using the ActiveEditObject property of the Application object to see if a sketch is active.

## Syntax

SketchedSymbolDefinitions.**Add**( ***Name*** As String ) As [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that defines name of the sketched symbol definition. The name specified must be unique with respect to the other sketched symbol definitions in the document. If a unique name is not specified, an error will occur. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |