# WorkPlanes.AddByPlaneAndPoint Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane that is parallel to the input plane and passes through the input point. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByPlaneAndPoint**( ***Plane*** As Object, ***Point*** As Object, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Point | Object | Input object that represents a point. This object can be a WorkPoint, Vertex or SketchPoint object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4
