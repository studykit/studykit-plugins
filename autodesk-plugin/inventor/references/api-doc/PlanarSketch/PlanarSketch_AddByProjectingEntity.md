# PlanarSketch.AddByProjectingEntity Method

Parent Object: [PlanarSketch](../PlanarSketch/PlanarSketch.md)

## Description

Method that creates a new sketch entity by projecting other entities onto the sketch plane. This method performs the same function as the Project Geometry or Project DWG Geometry command according to the Entity you specified.

## Syntax

PlanarSketch.**AddByProjectingEntity**( ***Entity*** As Object ) As [SketchEntity](../SketchEntity/SketchEntity.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input object to project onto the sketch plane. In a part context, valid input includes the various 2d sketch objects, the various 3d sketch objects, Edge, Vertex, WorkAxis, WorkPoints and DWGEntities. WorkPlanes that are perpendicular to the sketch are also valid. In an assembly context (where this method is called on a PlanarSketchProxy object) this method that projects an entity from one part into a sketch in another part. The valid input in this case includes the various 2d sketch proxy objects, the various 3d sketch proxy objects, EdgeProxy, VertexProxy, WorkAxisProxy, and WorkPointProxy objects. WorkPlaneProxy objects that are perpendicular to the sketch are also valid. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |