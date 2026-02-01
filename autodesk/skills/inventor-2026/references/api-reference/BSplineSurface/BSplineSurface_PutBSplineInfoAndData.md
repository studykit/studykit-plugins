# BSplineSurface.PutBSplineInfoAndData Method

Parent Object: [BSplineSurface](../BSplineSurface/BSplineSurface.md)

## Description

Sets the definition data of the spline surface.

## Syntax

BSplineSurface.**PutBSplineInfoAndData**( ***Order***() As Long, ***Poles***() As Double, ***KnotsU***() As Double, ***KnotsV***() As Double, ***Weights***() As Double, ***IsPeriodic***() As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input Long array of two elements that specifies the order of the spline in U and V respectively. |
| Poles | Double | Input/output Double that specifies the poles of the B-Spline. |
| KnotsU | Double | Input/output Double that specifies the knots of the B-Spline in U. |
| KnotsV | Double | Input/output Double that specifies the knots of the B-Spline in V. |
| Weights | Double | Input/output Double that specifies the B-spline's weights. |
| IsPeriodic | Boolean | Input/Output Boolean that specifies whether the B-Spline is periodic. |

## Version

Introduced in version 4
