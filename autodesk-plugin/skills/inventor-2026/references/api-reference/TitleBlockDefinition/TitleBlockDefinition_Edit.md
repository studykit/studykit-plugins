# TitleBlockDefinition.Edit Method

Parent Object: [TitleBlockDefinition](../TitleBlockDefinition/TitleBlockDefinition.md)

## Description

Method that opens a copy of the title block definition's sketch for edit in the Sketch environment. Returns \Output DrawingSketch created by copying the sketch associated with the title block definition.

## Remarks

The DrawingSketch returned is a new sketch that Autodesk Inventor creates by copying the sketch associated with the title block definition. The new sketch supports all edit operations. The ExitEdit method of the TitleBlockDefinition object can be used to replace the title block definition's sketch with the new sketch.

## Syntax

TitleBlockDefinition.**Edit**( ***Result*** As [DrawingSketch](../DrawingSketch/DrawingSketch.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Result | [DrawingSketch](../DrawingSketch/DrawingSketch.md) |  |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
