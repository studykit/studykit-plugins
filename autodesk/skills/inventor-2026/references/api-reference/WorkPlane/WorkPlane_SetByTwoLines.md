# WorkPlane.SetByTwoLines Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to be based on the two input lines.

## Remarks

Line1 defines the X axis. If the two lines are not in the same plane, the plane is calculated by crossing the vectors defined by Line1 and Line2. This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByTwoLines**( ***Line1*** As Object, ***Line2*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line1 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Line2 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |

## Version

Introduced in version 4
