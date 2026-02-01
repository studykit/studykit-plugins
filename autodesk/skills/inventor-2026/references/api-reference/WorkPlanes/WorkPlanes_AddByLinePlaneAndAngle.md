# WorkPlanes.AddByLinePlaneAndAngle Method

Parent Object: [WorkPlanes](../WorkPlanes/WorkPlanes.md)

## Description

Method that creates a new work plane through the input line at the specified angle from the input plane. This method is not currently supported when creating a work plane within an assembly.

## Syntax

WorkPlanes.**AddByLinePlaneAndAngle**( ***Line*** As Object, ***Plane*** As Object, ***Angle*** As Variant, [***Construction***] As Boolean ) As [WorkPlane](../WorkPlane/WorkPlane.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Angle | Variant | Input Variant that defines the offset angle of the work plane from the input plane. This can be a numeric value or a string. The offset angle of a work plane is always defined by a parameter. When a new work plane is created that requires a parameter, that parameter is automatically created when the work plane is created. If a numeric value is supplied the new parameter is set to the value specified. The input value is in radians. If a string is supplied it is used as the expression for the newly created parameter and will be interpreted the same as if the user entered it in a dialog. This means if a value is specified without a unit qualifier it will default to the current document length unit. The following is a valid entry for the angle, assuming the parameter d2 already exists and defines an angle, "d2 + 10 deg." The positive angle direction is computed by crossing the axis vector with the plane normal vector. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work plane as a construction plane or not. The default is False, which indicates to create a standard work plane, not a construction work plane. A construction work plane is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users. |

## Version

Introduced in version 4
