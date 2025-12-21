# BoundaryPatchLoops.Add Method

Parent Object: [BoundaryPatchLoops](../BoundaryPatchLoops/BoundaryPatchLoops.md)

## Description

Method that creates a new BoundaryPatchLoop object using the specified boundary path.

## Remarks

You can then use functionality provided by the resulting BoundaryPatchLoop object to access the entities that constitute the boundary loop and define the boundary conditions, if applicable, for these boundary entities.

## Syntax

BoundaryPatchLoops.**Add**( ***BoundaryPath*** As Object ) As [BoundaryPatchLoop](../BoundaryPatchLoop/BoundaryPatchLoop.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BoundaryPath | Object | Input Object that defines the boundary path for a boundary patch loop. Valid objects for the boundary path can be one of the following types:  One of the following objects: Path, Profile, Profile3D, EdgeLoop or EdgeCollection If a Path, Profile or Profile3D object is specified, then it must represent a set of connected sketch entities that form a closed loop, otherwise the creation of the boundary loop will fail. If an EdgeCollection object is specified, then it must contain a set of tangentially connected edges that form a closed loop, otherwise the creation of the boundary loop will fail.  An ObjectCollection that can contain any combination of SketchEntity, SketchEntity3D and Edge objects These objects can be used to specify a set of connected entities that form a closed boundary loop. Also, the order of the objects in the collection must be such that the entities that represent them are end-to-end connected. If the entities do not form a closed loop or if their order in the collection does not represent a set of end-to-end connected entities, then the creation of the boundary loop will fail. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |