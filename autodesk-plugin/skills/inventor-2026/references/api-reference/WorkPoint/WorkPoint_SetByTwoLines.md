# WorkPoint.SetByTwoLines Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines the work point to be at the intersection of the two input lines.

## Remarks

If the lines don't intersect an error will occur. This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetByTwoLines**( ***Line1*** As Object, ***Line2*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Line1 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |
| Line2 | Object | Input object that represents a line. This object can be a linear Edge, WorkAxis, SketchLine, or SketchLine3D object. |

## Version

Introduced in version 4
