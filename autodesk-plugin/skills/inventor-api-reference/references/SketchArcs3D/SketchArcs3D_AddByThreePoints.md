# SketchArcs3D.AddByThreePoints Method

Parent Object: [SketchArcs3D](../SketchArcs3D/SketchArcs3D.md)

## Description

Method that creates a new sketch arc that passes through the three input points. All the points must lie on the same plane.

## Syntax

SketchArcs3D.**AddByThreePoints**( ***StartPoint*** As Object, ***MidPoint*** As Object, ***EndPoint*** As Object ) As [SketchArc3D](../SketchArc3D/SketchArc3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input object that defines the start point. This can be either a SketchPoint3D or Point object. In the case where a SketchPoint3D object is input, that start point of the arc will be attached to the sketch point. |
| MidPoint | Object | Input Point object that defines a point along the arc. |
| EndPoint | Object | Input object that defines the end point. This can be either a SketchPoint3D or Point object. In the case where a SketchPoint3D object is input, that end point of the arc will be attached to the sketch point. |

## Version

Introduced in version 2008
