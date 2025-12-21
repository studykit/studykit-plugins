# Sketch.AddByProjectingEntity Method

Parent Object: [Sketch](../Sketch/Sketch.md)

## Description

Method that creates a new sketch entity by projecting other entities onto the sketch plane. This method performs the same function as the Project Geometry or Project DWG Geometry command according to the Entity you specified.

## Syntax

Sketch.**AddByProjectingEntity**( ***Entity*** As Object ) As [SketchEntity](../SketchEntity/SketchEntity.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input object to project onto the sketch plane. In a part context, valid input includes the various 2d sketch objects, the various 3d sketch objects, Edge, Vertex, WorkAxis, WorkPoints and DWGEntities. WorkPlanes that are perpendicular to the sketch are also valid. In an assembly context (where this method is called on a PlanarSketchProxy object) this method that projects an entity from one part into a sketch in another part. The valid input in this case includes the various 2d sketch proxy objects, the various 3d sketch proxy objects, EdgeProxy, VertexProxy, WorkAxisProxy, and WorkPointProxy objects. WorkPlaneProxy objects that are perpendicular to the sketch are also valid. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch from Face Silhouette](../../sample-programs/PlanarSketch_AddBySilhouette_Sample.md) | This sample creates a cylindrical solid, creates a new sketch plane and creates some new sketch lines from the actual edges and the apparent (silhouette) edges of the cylinder. |
| [Projection - project across parts](../../sample-programs/Sketch_AddByProjectingEntity_Sample.md) | This sample demonstrates projecting a sketch entity across parts in an assembly. To use the sample, have an assembly open that contains at least two occurrences, (parts only), and run the program. |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |