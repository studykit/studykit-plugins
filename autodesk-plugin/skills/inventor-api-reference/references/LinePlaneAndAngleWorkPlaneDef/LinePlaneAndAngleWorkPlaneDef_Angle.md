# LinePlaneAndAngleWorkPlaneDef.Angle Property

Parent Object: [LinePlaneAndAngleWorkPlaneDef](../LinePlaneAndAngleWorkPlaneDef/LinePlaneAndAngleWorkPlaneDef.md)

## Description

Property that returns the parameter controlling the angle of a line, plane and angle defined work plane. The angle of the plane can be read and modified by accessing the returned Parameter object. The positive angle direction is computed by crossing the axis vector with the plane normal vector. Changes made will not be visible until the model is recomputed.

## Syntax

LinePlaneAndAngleWorkPlaneDef.**Angle**() As [Parameter](../Parameter/Parameter.md)

## Property Value

This is a read only property whose value is a [Parameter](../Parameter/Parameter.md).

## Version

Introduced in version 4
