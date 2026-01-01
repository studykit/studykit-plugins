# WorkPlane.SetByPointAndTangent Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to pass through the input point and tangent to the input surface.

## Remarks

This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByPointAndTangent**( ***Point*** As Object, ***Face*** As [Face](../Face/Face.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | Object | Input object that represents a point. This object can be a Vertex, WorkPoint, SketchPoint3D or SketchPoint object. The input point must lie on the input surface. |
| Face | [Face](../Face/Face.md) | Input Face object that indicates the tangent surface. This face must either be a cylinder, a cone that is positioned such that a valid tangent exists, a sphere or a bspline surface. |

## Version

Introduced in version 2008
