# LinePlaneAndAngleWorkPlaneDef.GetData Method

Parent Object: [LinePlaneAndAngleWorkPlaneDef](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef.md)

## Description

Method that gets all of the data defining a work planed defined by a line, plane and an angle. The work plane passes through the line and is a specified angle to the plane.

## Syntax

LinePlaneAndAngleWorkPlaneDef.**GetData**( ***Line*** As Object, ***Plane*** As Object, ***Angle*** As [Parameter](../Parameter/Parameter.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line | Object | Output object that represents a line. This object can be a linear Edge, WorkAxis, or SketchLine object. The work plane passes through this line. |
| Plane | Object | Output object that represents a plane. This object can be a planar Face, WorkPlane, or Sketch object. The angle of the work plane is measured with respect to this plane. |
| Angle | [Parameter](../Parameter/Parameter.md) | Output Parameter that defines the angle of the work plane to the plane. The positive angle direction is computed by crossing the axis vector with the plane normal vector. |

## Version

Introduced in version 4
