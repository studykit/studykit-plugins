# SketchCircles.AddByCenterRadius Method

Parent Object: [SketchCircles](../SketchCircles/SketchCircles.md)

## Description

Method that creates a new sketch circle at a specified location and radius.

## Syntax

SketchCircles.**AddByCenterRadius**( ***CenterPoint*** As Object, ***Radius*** As Double ) As [SketchCircle](../SketchCircle/SketchCircle.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the circle will be attached to the point. |
| Radius | Double | Input Double that defines the radius of the circle in centimeters. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Sketch fill region](../../sample-programs/DrawingSketch_SketchFillRegions_Sample.md) | This sample demonstrates the sketch fill functionality in drawing sketches. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Add iMate Definition](../../sample-programs/iMateDefinitions_AddMateiMateDefinition_Sample.md) | Add iMate definitions using AddMateiMateDefinition and AddInsertiMateDefinition. |
| [Moving sketch entities to a new layer](../../sample-programs/Layer_Sample.md) | This sample demonstrates the creation of a new layer and moving sketch entities onto this newly created layer. |
| [Create sheet metal lofted flange feature](../../sample-programs/LoftedFlangeFeatures_Add_Sample.md) | The following sample demonstrates the creation of a sheet metal lofted flange feature. |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Sketch Edit Orientation](../../sample-programs/PlanarSketch_NaturalAxisDirection_Sample.md) | This sample demonstrates modifying the orientation of a sketch. |
| [Sketch Add Oriented](../../sample-programs/PlanarSketches_AddWithOrientation_Sample.md) | This sample demonstrates the creation of a sketch using the Sketches.AddWithOrientation method. |
| [Sketch profile control](../../sample-programs/ProfilePath_AddsMaterial_Sample.md) | This sample demonstrates the usage of the Profiles API to control the shape of the profile. The sample creates three concntric circles and creates an extrusion of the region between the inner circles. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Sweep Feature Add](../../sample-programs/SweepFeature_Sample.md) | This sample demonstrates the creation of a sweep feature. The profile is a circle, but the path is made up of a 3D sketch and a 2D sketch. |
| [Thread Feature Create](../../sample-programs/ThreadFeature_Sample.md) | This sample demonstrates the creation of a thread feature. It creates a cylinder in a new part document and creates a thread feature on the cylinder. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |