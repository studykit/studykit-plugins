# SketchCircles Object

## Description

The SketchCircles object provides access to all the objects in a sketch and provides methods to create additional sketch circles. See the article in the overviews section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddByCenterRadius](../SketchCircles/SketchCircles_AddByCenterRadius.md) | Method that creates a new sketch circle at a specified location and radius. |
| [AddByThreePoints](../SketchCircles/SketchCircles_AddByThreePoints.md) | Method that creates a new sketch circle passing through the three input points. The three points are any three points along the perimeter of the desired circle. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SketchCircles/SketchCircles_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../SketchCircles/SketchCircles_Count.md) | Property that returns the number of items in this collection. |
| [Item](../SketchCircles/SketchCircles_Item.md) | Returns the specified SketchCircle object from the collection. |
| [Type](../SketchCircles/SketchCircles_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DrawingSketch.SketchCircles](../DrawingSketch/DrawingSketch_SketchCircles.md), [PlanarSketch.SketchCircles](../PlanarSketch/PlanarSketch_SketchCircles.md), [PlanarSketchProxy.SketchCircles](../PlanarSketchProxy/PlanarSketchProxy_SketchCircles.md), [Sketch.SketchCircles](../Sketch/Sketch_SketchCircles.md), [SketchBlockDefinition.SketchCircles](../SketchBlockDefinition/SketchBlockDefinition_SketchCircles.md), [SketchBlockDefinitionProxy.SketchCircles](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_SketchCircles.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SurfaceBody Copy](../../sample-programs/CopyBodyFeature_Sample.md) | This sample demonstrates copying a surface body from one part to another. This is equivalent to the Promote command, but the API is much more flexible. In order for the sample to be self-contained, it creates two parts on the fly that will be used to demonstrate copying a body from one part to another. When copying a body into a part, you provide the surface body and a matrix to define its position in the new part. This sample creates a matrix based on the position of these parts within an assembly. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
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