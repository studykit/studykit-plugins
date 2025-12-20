# TransientGeometry.CreateBSplineCurve2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new BSplineCurve2d object. The definition of the curve is supplied using the input \arguments. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateBSplineCurve2d**( ***Order*** As Long, ***Poles***() As Double, ***Knots***() As Double, ***Weights***() As Double, ***IsPeriodic*** As Boolean ) As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Output Long that specifies the order of the spline. |
| Poles | Double | Input/output Double that specifies the poles of the B\-Spline. |
| Knots | Double | Input/output Double that specifies the knots of the B\-Spline. |
| Weights | Double | Input/output Double that specifies the B\-spline's weights. |
| IsPeriodic | Boolean | Input Boolean that specifies whether the B\-Spline curve is periodic. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |