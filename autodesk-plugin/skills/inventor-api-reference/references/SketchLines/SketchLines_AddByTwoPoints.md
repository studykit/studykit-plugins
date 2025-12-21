# SketchLines.AddByTwoPoints Method

Parent Object: [SketchLines](../SketchLines/SketchLines.md)

## Description

Method that creates a new sketch line based on the two input points. The new sketch line is returned.

## Syntax

SketchLines.**AddByTwoPoints**( ***StartPoint*** As Object, ***EndPoint*** As Object ) As [SketchLine](../SketchLine/SketchLine.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input object that defines the start point of the line. This can be either a Point2d object defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, that point becomes the line's start point. |
| EndPoint | Object | Input object that defines the end point of the line. This can be either a Point2d object defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, that point becomes the line's end point. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |
| [Border Create and Insert](../../sample-programs/DrawingDocument_BorderDefinitions_Sample.md) | This sample illustrates creating a new border definition object and using it for a sheet. |
| [Drawing Sketches - editing line type and color](../../sample-programs/DrawingSketch_Sample.md) | This sample demonstrates the modification of sketch entity line type and color in drawings. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Defer sketch updates](../../sample-programs/Sketch_DeferUpdates_Sample.md) | This sample demonstrates the sketch defer update functionality. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |