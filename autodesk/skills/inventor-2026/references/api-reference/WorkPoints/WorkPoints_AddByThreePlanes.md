# WorkPoints.AddByThreePlanes Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Method that creates a new work point at the intersection of the three input planes. If the three input planes don't intersect an error will occur. This method is not currently supported when creating a work point within an assembly.

## Syntax

WorkPoints.**AddByThreePlanes**( ***Plane1*** As Object, ***Plane2*** As Object, ***Plane3*** As Object, [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane1 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Plane2 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Plane3 | Object | Input object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 6
