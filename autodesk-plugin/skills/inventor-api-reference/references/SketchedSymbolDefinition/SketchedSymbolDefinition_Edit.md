# SketchedSymbolDefinition.Edit Method

Parent Object: [SketchedSymbolDefinition](../SketchedSymbolDefinition/SketchedSymbolDefinition.md)

## Description

Method that opens a copy of the sketched symbol definition's sketch for edit in the Sketch environment. The DrawingSketch returned is a new sketch that Autodesk Inventor creates by copying the sketch associated with the sketched symbol definition. Returns \Output DrawingSketch created by copying the sketch associated with the sketched symbol definition.

## Remarks

The new sketch supports all edit operations. The ExitEdit method of the SketchedSymbolDefinition object can be used to replace the sketched symbol definition's sketch with the new sketch.

## Syntax

SketchedSymbolDefinition.**Edit**( ***Result*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Result | [DrawingSketch](../DrawingSketch/DrawingSketch.md) | Output DrawingSketch object. This DrawingSketch is a copy of the DrawingSketch associated with the sketched symbol definition. This new DrawingSketch is opened within the sketch environment. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |

## Version

Introduced in version 5.3
