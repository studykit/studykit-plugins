# BSplineCurve2d.PutBSplineInfoAndData Method

Parent Object: [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Description

Sets the definition data of the spline.

## Syntax

BSplineCurve2d.**PutBSplineInfoAndData**( ***Order*** As Long, ***Poles***() As Double, ***Knots***() As Double, ***Weights***() As Double, ***IsPeriodic*** As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input Long array of two elements that specifies the order of the spline in U and V respectively. |
| Poles | Double | Input/output Double that specifies the poles of the B-Spline. |
| Knots | Double | Input/output Double that specifies the knots of the B-Spline. |
| Weights | Double | Input/output Double that specifies the B-spline's weights. |
| IsPeriodic | Boolean | Input Boolean that specifies whether the B-Spline is periodic. |

## Version

Introduced in version 4
