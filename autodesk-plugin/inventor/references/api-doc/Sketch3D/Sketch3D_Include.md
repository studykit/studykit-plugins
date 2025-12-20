# Sketch3D.Include Method

Parent Object: [Sketch3D](../Sketch3D/Sketch3D.md)

## Description

Method that creates a new sketch entity by copying other entities into the sketch.

## Syntax

Sketch3D.**Include**( ***Entity*** As Object ) As [SketchEntity3D](../SketchEntity3D/SketchEntity3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Entity | Object | Input object to copy into the sketch. In a part context, valid input includes Edges, 3d sketch entities and planar sketch entities. In an assembly context (where this method is called on a Sketch3DProxy object) this method that includes an entity from one part into a sketch in another part. The valid input in this case includes EdgeProxy objects, the various 3d sketch proxy objects and the various 2d sketch proxy objects. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |