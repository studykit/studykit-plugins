# BSplineCurve2d.GetBSplineInfo Method

Parent Object: [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Description

Gets general information about the definition of the spline, including its order, number of poles and knots, and its rational, periodic, closed, and planar states.

## Syntax

BSplineCurve2d.**GetBSplineInfo**( ***Order*** As Long, ***NumPoles*** As Long, ***NumKnots*** As Long, ***IsRational*** As Boolean, ***IsPeriodic*** As Boolean, ***IsClosed*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Output Long that specifies the order of the spline. |
| NumPoles | Long | Output Long that specifies the number of poles. |
| NumKnots | Long | Output Long that specifies the number of knots. |
| IsRational | Boolean | Output Boolean that specifies whether the B-Spline is rational. |
| IsPeriodic | Boolean | Output Boolean that specifies whether the B-Spline is periodic. |
| IsClosed | Boolean | Output Boolean that specifies whether the curve is closed. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |