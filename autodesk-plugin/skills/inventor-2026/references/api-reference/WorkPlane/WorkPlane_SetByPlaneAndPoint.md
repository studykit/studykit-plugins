# WorkPlane.SetByPlaneAndPoint Method

Parent Object: [WorkPlane](../WorkPlane/WorkPlane.md)

## Description

Method that redefines the work plane to be parallel to the input plane and passing through the input point.

## Remarks

This method is not valid when the work plane exists in an Assembly component definition.

## Syntax

WorkPlane.**SetByPlaneAndPoint**( ***Plane*** As Object, ***Point*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Plane | Object | Input object that represents a Plane. This object can be a planar Face, WorkPlane, or Sketch object. |
| Point | Object | Input object that represents a point. This object can be a WorkPoint, Vertex, SketchPoint, or SketchPoint3D object. |

## Version

Introduced in version 4
