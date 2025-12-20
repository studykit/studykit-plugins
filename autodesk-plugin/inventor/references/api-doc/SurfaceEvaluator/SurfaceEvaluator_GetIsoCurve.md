# SurfaceEvaluator.GetIsoCurve Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Function that extracts a curve from the surface that follows a constant u or v parameter along the surface. It will have the same properties of the surface in the direction of the extraction. For example, if a curve is extracted from a periodic surface in the direction where it is periodic, the extracted curve will also be periodic. The type of curve returned is dependent on the shape the surface.

## Remarks

The return is an ObjectCollection that can contain one or more curves. Multiple curves are returned in the case where the SurfaceEvaluator is obtained from a Face and the curve cuts across internal boundaries. The resulting curve is trimmed to the boundaries and will result in multiple curves. If the SurfaceEvaluator is obtained from a geometry object then a single curve is always returned because there are no boundaries to trim the curve. The type of curve(s) returned is dependent on the shape of the input curve and the surface.

## Syntax

SurfaceEvaluator.**GetIsoCurve**( ***Parameter*** As Double, ***UDirection*** As Boolean ) As [ObjectCollection](../ObjectCollection/ObjectCollection.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Parameter | Double | Input Double that specifies the parameter value to indicate where the curve should be extracted. It can be either a U or V parameter depending on the value of the next argument. |
| UDirection | Boolean | Input Boolean indicating if the parameter value is a U or V parameter value. If True, then the parameter value is a V parameter indicating that the position of the U iso curve. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |