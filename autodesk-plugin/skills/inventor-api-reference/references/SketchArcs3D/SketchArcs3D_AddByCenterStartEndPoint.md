# SketchArcs3D.AddByCenterStartEndPoint Method

Parent Object: [SketchArcs3D](../SketchArcs3D/SketchArcs3D.md)

## Description

Method that creates a new sketch arc defined by a center point and two points defining the start and end. Method that creates a new sketch arc defined by a center point and two points defining the start and end.

## Remarks

The input points can be a combination of existing sketch points or Point objects. In the case where a sketch points is input, the arc will be attached to the sketch point. The sweep direction of the arc from the start to end point is determined by the CounterClockwise argument. The radius of the arc is determined by the start point. If the input for the start point is a sketch point, the arc will be tied to the sketch point. The second point, whether it is a sketch point or coordinate point defines the sweep of the arc. In the case where a sketch point is input and it is on the arc, the arc will be tied to the sketch point.

## Syntax

SketchArcs3D.**AddByCenterStartEndPoint**( ***CenterPoint*** As Object, ***StartPoint*** As Object, ***EndPoint*** As Object, [***Normal***] As Variant, [***CounterClockwise***] As Boolean ) As [SketchArc3D](../SketchArc3D/SketchArc3D.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| CenterPoint | Object | Input object that defines the center point. This can currently only be a Point object. |
| StartPoint | Object | Input object that defines the start point. This can be either a SketchPoint3D or Point object. In the case where a SketchPoint3D object is input, the start point of the arc will be attached to the sketch point. |
| EndPoint | Object | Input object that defines the end point. This can be either a SketchPoint3D or Point object. In the case where a SketchPoint3D object is input and the point lies on the arc, the end point of the arc will be attached to the sketch point. |
| Normal | Variant | Optional input UnitVector that defines the normal direction for the arc. This is only required when the start, center and end points are collinear (i.e. the arc is a semi-circle). In other cases, the normal need not be provided, but if it is, it needs to be consistent with the input points. |
| CounterClockwise | Boolean | Optional input Boolean that defines whether the arc sweeps in a clockwise or counterclockwise direction between the start and end points. The default value is True which indicates a counterclockwise sweep direction.   This is an optional argument whose default value is False. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |