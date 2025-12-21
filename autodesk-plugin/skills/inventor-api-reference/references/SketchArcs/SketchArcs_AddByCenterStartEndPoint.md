# SketchArcs.AddByCenterStartEndPoint Method

Parent Object: [SketchArcs](../SketchArcs/SketchArcs.md)

## Description

Method that creates a new sketch arc defined by a center point and two points defining the start and end. The input points can be a combination of existing sketch points or Point2d objects. In the case where a sketch points is input, the arc will be attached to the sketch point. The sweep direction of the arc from the start to end point is determined by the CounterClockwise argument. The radius of the arc is determined by the start point. If the input for the start point is a sketch point, the arc will be tied to the sketch point. The second point, whether it is a sketch point or coordinate point defines the sweep of the arc. In the case where a sketch point is input and it is on the arc, the arc will be tied to the sketch point.

## Syntax

SketchArcs.**AddByCenterStartEndPoint**( ***CenterPoint*** As Object, ***StartPoint*** As Object, ***EndPoint*** As Object, [***CounterClockwise***] As Boolean ) As [SketchArc](../SketchArc/SketchArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the center point of the arc will be attached to the sketch point. |
| StartPoint | Object | Input object that defines the start point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, the start point of the arc will be attached to the sketch point. |
| EndPoint | Object | Input object that defines the end point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input and the point lies on the arc, the end point of the arc will be attached to the sketch point. |
| CounterClockwise | Boolean | Optional input Boolean that defines whether the arc sweeps in a clockwise or counterclockwise direction between the start and end points. The default value is True which indicates a counterclockwise sweep direction. |

## Version

Introduced in version 5
