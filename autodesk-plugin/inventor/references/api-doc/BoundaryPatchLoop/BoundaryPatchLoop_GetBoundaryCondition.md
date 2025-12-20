# BoundaryPatchLoop.GetBoundaryCondition Method

Parent Object: [BoundaryPatchLoop](../BoundaryPatchLoop/BoundaryPatchLoop.md)

## Description

Method that gets the boundary condition for the specified boundary path loop entity.

## Remarks

The method returns a constant that indicates the boundary condition that has been applied. The constant is one of the values in BoundaryPatchConditionEnum: kFreeBoundaryPatchCondition or kTangentBoundaryPatchCondition.

## Syntax

BoundaryPatchLoop.**GetBoundaryCondition**( ***BoundaryPathEntity*** As Object ) As [BoundaryPatchConditionEnum](../BoundaryPatchConditionEnum.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BoundaryPathEntity | Object | Input object that specifies the boundary path loop entity for which the boundary condition needs to be returned. If a boundary condition is not applicable to the boundary path entity, then this method will fail. The valid objects for the boundary path entity depend on the type of the boundary path object, i.e. the object returned by the BoundaryPath property. The following list shows the valid BoundaryPathEntity objects for the corresponding BoundaryPath object: \* If BoundaryPath object is Profile3D, then the BoundaryPathEntity object can be one of the sketch 3D entities that constitute the Profile3D. \* If BoundaryPath object is Path, then the BoundaryPathEntity object can be one of the sketch 2D or 3D entities that constitute the Path. \* If BoundaryPath object is EdgeLoop, then the BoundaryPathEntity object can be one of the edges that constitute the EdgeLoop. \* If BoundaryPath object is EdgeCollection, then the BoundaryPathEntity object can be one of the edges that belong to the EdgeCollection. \* If BoundaryPath object is an ObjectCollection that contains SketchEntity, SketchEntity3D or Edge objects, then the BoundaryPathEntity object can be one of the entities that belong to the ObjectCollection. |

## Notes

If the boundary path object, i.e. the object returned by the BoundaryPath property is a Profile then the boundary condition does not apply. If the Profile object or one of the sketch 2D entities that constitute the profile is specified for the BoundaryPathEntity argument then, this method will fail.

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |