# SketchLines Object

## Description

The SketchLines object provides access to all of the objects in a sketch and provides methods to create additional sketch lines. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddAsPolygon](../SketchLines/SketchLines_AddAsPolygon.md) | Method that creates a polygon with up to 120 sides. The sketch lines representing the polygon are returned. |
| [AddAsThreePointCenteredRectangle](../SketchLines/SketchLines_AddAsThreePointCenteredRectangle.md) | Method that creates four lines to represent a rectangle where the center of the rectangle is defined by a point, the length and orientation is defined by a second point, and the width defined by a third point. |
| [AddAsThreePointRectangle](../SketchLines/SketchLines_AddAsThreePointRectangle.md) | Method that creates four lines to represent a rectangle where the base of the rectangle is defined by two points and the height is defined by a third point. The input points for the base can be either Point2d objects defining an X-Y point in space, or an existing SketchPoint object. |
| [AddAsTwoPointCenteredRectangle](../SketchLines/SketchLines_AddAsTwoPointCenteredRectangle.md) | Method that creates four lines to represent a rectangle where the center of the rectangle is defined by a point and the corner of the rectangle is defined by the second point and the rectangle is aligned with the sketch x and y axes. The input points can be either Point2d objects defining an x-y point in space, or an existing SketchPoint object. If an existing sketch point is input, the lines will become connected to that point. The created sketch lines are returned in a SketchEntitiesEnumerator object. This includes the four lines representing the rectangle and the two internal construction lines. |
| [AddAsTwoPointRectangle](../SketchLines/SketchLines_AddAsTwoPointRectangle.md) | Method that creates four lines to represent a rectangle where the diagonal corners of the rectangle are defined by the two input points and the rectangle is aligned with the sketch X and Y axes. The four new sketch lines are returned in an SketchEntitiesEnumerator object. |
| [AddByMidEndPoints](../SketchLines/SketchLines_AddByMidEndPoints.md) | Method that creates a new sketch line based on the mid and end points. The new sketch line is returned. |
| [AddByTwoPoints](../SketchLines/SketchLines_AddByTwoPoints.md) | Method that creates a new sketch line based on the two input points. The new sketch line is returned. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchLines/SketchLines_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchLines/SketchLines_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchLines/SketchLines_Item.md) | Returns the specified SketchLine object from the collection. |
| [Type](../SketchLines/SketchLines_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.SketchLines](../DrawingSketch/DrawingSketch_SketchLines.md), [PlanarSketch.SketchLines](../PlanarSketch/PlanarSketch_SketchLines.md), [PlanarSketchProxy.SketchLines](../PlanarSketchProxy/PlanarSketchProxy_SketchLines.md), [Sketch.SketchLines](../Sketch/Sketch_SketchLines.md), [SketchBlockDefinition.SketchLines](../SketchBlockDefinition/SketchBlockDefinition_SketchLines.md), [SketchBlockDefinitionProxy.SketchLines](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchLines.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |
| [Using Inventor's error dialog](../../sample-programs/ErrorManager_Sample.md) | Demonstrates using Inventor's error dialog. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Create sheet metal face and fold features](../../sample-programs/FoldFeatures_Add_Sample.md) | This sample demonstrates the creation of sheet metal face and fold features. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |
| [Defer sketch updates](../../sample-programs/Sketch_DeferUpdates_Sample.md) | This sample demonstrates the sketch defer update functionality. |
| [Sketch Lines](../../sample-programs/Sketch_SketchLines_Sample.md) | This sample demonstrates creating lines. It uses all of the various methods to create lines, both singly and as rectangles. |
| [Create and insert a sketch block definition into a part sketch](../../sample-programs/SketchBlockDefinition_Sample.md) | This sample demonstrates inserting a sketch block into a part sketch. |
| [Create sketch block from an existing sketch](../../sample-programs/SketchBlocks_Add_Sample.md) | This sample demonstrates creating a sketch block from an existing sketch. |
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