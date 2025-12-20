# TransientGeometry.CreatePolyline3dFromCurve Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Polyline3d object by approximating the input curve within the specified tolerance. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreatePolyline3dFromCurve**( ***Curve*** As Object, ***Tolerance*** As Double ) As [Polyline3d](../Polyline3d/Polyline3d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Curve | Object | Input transient geometry curve that will be approximated. Valid input for this argument is an Arc3d, BSplineCurve, Circle, EllipseFull, EllipticalArc, and LineSegment. |
| Tolerance | Double | Input Double defining the approximation tolerance. This value is in centimeters. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |