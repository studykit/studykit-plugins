# BoundaryPatchLoop.SetBoundaryCondition Method

Parent Object: [BoundaryPatchLoop](../BoundaryPatchLoop/BoundaryPatchLoop.md)

## Description

Method that sets the boundary condition for the specified boundary path loop entity.

## Syntax

BoundaryPatchLoop.**SetBoundaryCondition**( ***BoundaryPathEntity*** As Object, ***BoundaryPathCondition*** As [BoundaryPatchConditionEnum](../BoundaryPatchConditionEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| BoundaryPathEntity | Object | Input object that specifies the boundary path loop entity to which the boundary condition needs to be applied. If a boundary condition is not applicable to the boundary path entity, then this method will fail. The valid objects for the boundary path entity depend on the type of the boundary path object, i.e. the object returned by the BoundaryPath property. The following table lists the valid BoundaryPathEntity objects for the corresponding BoundaryPath object:  If BoundaryPath object is: Then, the BoundaryPathEntity object can be:  Profile3D One of the sketch 3D entities that constitute the Profile3D  Path One of the sketch 2D or 3D entities that constitute the Path  EdgeLoop One of the edges that constitute the EdgeLoop  EdgeCollection One of the edges that belong to the EdgeCollection  ObjectCollection that contains SketchEntity, SketchEntity3D or Edge objects One of the entities that belong to the ObjectCollectionNote: If the boundary path object, i.e. the object returned by the BoundaryPath property is a Profile then the boundary condition does not apply. If the Profile object or one of the sketch 2D entities that constitute the profile is specified for the BoundaryPathEntity argument then, this method will fail. |
| BoundaryPathCondition | [BoundaryPatchConditionEnum](../BoundaryPatchConditionEnum.md) | Input constant that specifies the type of boundary condition to apply. Valid input is one of the values in BoundaryPatchConditionEnum: kFreeBoundaryPatchCondition or kTangentBoundaryPatchCondition. If the specified condition cannot be applied to the boundary path entity, then this method will fail. |

## Notes

If the boundary path object, i.e. the object returned by the BoundaryPath property is a Profile then the boundary condition does not apply. If the Profile object or one of the sketch 2D entities that constitute the profile is specified for the BoundaryPathEntity argument then, this method will fail. If the specified condition cannot be applied to the boundary path entity, then this method will fail.

## Version

Introduced in version 2008
