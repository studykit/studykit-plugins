# WorkAxes.AddByLineAndPlane Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis that is along a line defined by projecting the input line onto the input plane along the plane normal. This method is not currently supported when creating a work axis within an assembly.

## Syntax

WorkAxes.**AddByLineAndPlane**( ***Line*** As Object, ***Plane*** As Object, [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input line object to project along the plane. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Plane | Object | Input plane object along which to project the line. This object can be a planar Face, WorkPlane, or Sketch object. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis, not a construction work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction: \* Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. \* If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4
