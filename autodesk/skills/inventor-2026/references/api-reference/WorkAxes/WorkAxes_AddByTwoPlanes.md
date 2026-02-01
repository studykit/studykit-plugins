# WorkAxes.AddByTwoPlanes Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis at the intersection of the two input planes. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByTwoPlanes**( ***Plane1*** As Object, ***Plane2*** As Object, [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane1 | Object | First input plane object for which to find the intersection at which to create the work axis. This object can be a planar Face, WorkPlane, or Sketch object. |
| Plane2 | Object | Second input plane object for which to find the intersection at which to create the work axis. This object can be a planar Face, WorkPlane, or Sketch object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis, not a construction work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction: \* Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. \* If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4
