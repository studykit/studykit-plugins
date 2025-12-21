# BorderDefinition.Edit Method

Parent Object: [BorderDefinition](../BorderDefinition/BorderDefinition.md)

## Description

Method that opens a copy of the border definition's sketch for edit in the Sketch environment.

## Remarks

The DrawingSketch returned is a new sketch that Autodesk Inventor creates by copying the sketch associated with the border definition. The new sketch supports all edit operations. The ExitEdit method of the BorderDefinition object can be used to replace the border definition's sketch with the new sketch.

## Syntax

BorderDefinition.**Edit**( ***Sketch*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Sketch | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Output DrawingSketch object. This is a copy of the DrawingSketch associated with the border definition. This new DrawingSketch is opened within the sketch environment. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |

## Version

Introduced in version 5.3

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |