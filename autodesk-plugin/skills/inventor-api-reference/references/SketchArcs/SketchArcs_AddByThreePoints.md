# SketchArcs.AddByThreePoints Method

Parent Object: [SketchArcs](../SketchArcs/SketchArcs.md)

## Description

Method that creates a new sketch arc that passes through the three input points.

## Syntax

SketchArcs.**AddByThreePoints**( ***StartPoint*** As Object, ***MidPoint*** As [Point2d](../Point2d/Point2d.md), ***EndPoint*** As Object ) As [SketchArc](../SketchArc/SketchArc.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| StartPoint | Object | Input object that defines the start point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, that start point of the arc will be attached to the sketch point. |
| MidPoint | [Point2d](../Point2d/Point2d.md) | Input Point2d object that defines a point along the arc. |
| EndPoint | Object | Input object that defines the end point. This can be either a SketchPoint or Point2d object. In the case where a SketchPoint object is input, that end point of the arc will be attached to the sketch point. |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |