# BSplineCurve.PutBSplineInfoAndData Method

Parent Object: [BSplineCurve](../BSplineCurve/BSplineCurve.md)

## Description

Sets the definition data of the spline.

## Syntax

BSplineCurve.**PutBSplineInfoAndData**( ***Order*** As Long, ***Poles***() As Double, ***Knots***() As Double, ***Weights***() As Double, ***IsPeriodic*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input Long that specifies the order of the spline. |
| Poles | Double | Input/output Double that specifies the poles of the B-Spline. |
| Knots | Double | Input/output Double that specifies the knots of the B-Spline. |
| Weights | Double | Input/output Double that specifies the B-spline's weights. |
| IsPeriodic | Boolean | Input Boolean that specifies whether the B-Spline is periodic. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |