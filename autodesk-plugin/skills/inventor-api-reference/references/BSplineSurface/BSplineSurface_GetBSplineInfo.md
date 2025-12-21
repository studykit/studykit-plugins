# BSplineSurface.GetBSplineInfo Method

Parent Object: [BSplineSurface](../BSplineSurface/BSplineSurface.md)

## Description

Gets general information about the definition of the spline, including its order, number of poles and knots, and its rational, periodic, closed, and planar states.

## Syntax

BSplineSurface.**GetBSplineInfo**( ***Order***() As Long, ***NumPoles***() As Long, ***NumKnots***() As Long, ***IsRational*** As Boolean, ***IsPeriodic***() As Boolean, ***IsClosed***() As Boolean, ***IsPlanar*** As Boolean, ***PlaneVector***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input Long array of two elements that specifies the order of the spline in U and V respectively. |
| NumPoles | Long | Input/output Long that specifies the number of poles. |
| NumKnots | Long | Input/output array of Longs that specifies the number of knots. |
| IsRational | Boolean | Output Boolean that specifies whether the B-Spline is rational. |
| IsPeriodic | Boolean | Input/Output Boolean that specifies whether the B-Spline is periodic. |
| IsClosed | Boolean | Input/Output Boolean that specifies whether the curve is closed. |
| IsPlanar | Boolean | Output Boolean that specifies whether the B-Spline is planar. |
| PlaneVector | Double | Output Double that specifies the B-Spline's plane vector. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |