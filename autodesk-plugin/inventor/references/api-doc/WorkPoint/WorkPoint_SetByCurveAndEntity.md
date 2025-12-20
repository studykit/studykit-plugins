# WorkPoint.SetByCurveAndEntity Method

Parent Object: [WorkPoint](../WorkPoint/WorkPoint.md)

## Description

Method that redefines a work point to be at the intersection of the input curve and an entity.

## Remarks

If the curve and entity don't intersect an error will occur. This method is not valid when the work point exists in an Assembly component definition.

## Syntax

WorkPoint.**SetByCurveAndEntity**( ***Curve*** As Object, ***Entity*** As Object, [***ProximityPoint***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object that represents a curve. This object can be an edge or a 2d or 3d sketch entity. |
| Entity | Object | Input object that will be intersected with the curve. This object can be a face or a work plane. There is a current limitation that this must be a planar face or work plane when anything but a line is input as the curve. Any face can be used when the curve is a line. |
| ProximityPoint | Variant | Optional input Point object that indicates multiple solutions to use. For example, a circle can intersect a plane twice, or a spline can intersect multiple times. If this argument is supplied, the result closest to the input point will be used. If this argument is not supplied and multiple solutions are possible, one solution will be arbitrarily chosen. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |