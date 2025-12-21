# WorkPlaneProxy.SetByLinePlaneAndAngle Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that redefines the work plane to be through the input line at the specified angle from the input plane.

## Syntax

WorkPlaneProxy.**SetByLinePlaneAndAngle**( ***Line*** As Object, ***Plane*** As Object, ***Angle*** As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Angle | Variant | Input Variant that defines the offset angle of the work plane from the input plane. This can be a numeric value or a string. The offset angle of a work plane is always defined by a parameter. When a new work plane is created, the parameter is automatically created. If a numeric value is supplied the new parameter is set to the value specified and the value is always in radians. If a string is supplied it is used as the expression for the newly created parameter and will be interpreted the same as if the user entered it in a dialog. This means if a value is specified without a unit qualifier it will default to the current document length unit. The following is a valid entry for the angle, assuming the parameter d2 already exists and defines an angle, 'd2 + 10 deg'. The positive angle direction is computed by crossing the axis vector with the plane normal vector. |

## Version

Introduced in version 2008
