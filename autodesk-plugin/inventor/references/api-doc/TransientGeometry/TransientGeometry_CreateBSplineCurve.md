# TransientGeometry.CreateBSplineCurve Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new BSplineCurve object. The definition of the curve is supplied using the input arguments. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateBSplineCurve**( ***Order*** As Long, ***Poles***() As Double, ***Knots***() As Double, ***Weights***() As Double, ***IsPeriodic*** As Boolean ) As [BSplineCurve](../BSplineCurve/BSplineCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Order | Long | Input Long that specifies the order of the curve. |
| Poles | Double | Input array of Doubles that contains the coordinates of the curve. The array contains sequential X, Y, Z coordinates. The number of poles is inferred by the size of the array. |
| Knots | Double | Input array of Doubles that contains the knot vectors of the curve. |
| Weights | Double | Input array of Doubles that contains the weight factor for each pole. If the curve is non-rational this argument is ignored. |
| IsPeriodic | Boolean | Input Boolean that specifies if the curve is periodic or not. True if it is periodic False if it is non-periodic. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |