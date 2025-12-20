# WorkPoints.AddByCurveAndEntity Method

Parent Object: [WorkPoints](../WorkPoints/WorkPoints.md)

## Description

Method that creates a new work point at the intersection of the input curve and entity. This method is not currently supported when creating a work point within an assembly.

## Remarks

If the curve and entity don't intersect an error will occur. A current limitation is that intersections between entities that are non-planar can only be performed with linear curves.

## Syntax

WorkPoints.**AddByCurveAndEntity**( ***Curve*** As Object, ***Entity*** As Object, [***ProximityPoint***] As Variant, [***Construction***] As Boolean ) As [WorkPoint](../WorkPoint/WorkPoint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input object that represents a curve. This object can be an edge or a 2d or 3d sketch entity. |
| Entity | Object | Input object that will be intersected with the curve. This object can be a face or a work plane. There is a current limitation that this must be a planar face or work plane when anything but a line is input as the curve. Any face can be used when the curve is a line. |
| ProximityPoint | Variant | Input Point object that indicates multiple solutions to use. For example, a circle can intersect a plane twice, or a spline can intersect multiple times. If this argument is supplied, the result closest to the input point will be used. If this argument is not supplied and multiple solutions are possible, one solution will be arbitrarily chosen. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work point as a construction point or not. The default is False, which indicates to create a standard work point. A construction work point is hidden from the user and is not displayed graphically or listed in the browser. If work features are created as construction:  * Deleting any downstream feature that consumes this construction work feature will have the effect of deleting this work feature as well. * If there are no consumers of the construction work feature, it is the responsibility of the creator to delete them since they will never get cleaned up and are not visible to users.     This is an optional argument whose default value is False. |

## Version

Introduced in version 6

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |