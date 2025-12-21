# TransientGeometry.CreateFittedBSplineCurve Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new object using fit points. The definition of the curve is supplied using the input definition object. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateFittedBSplineCurve**( ***Definition*** As [BSplineCurveDefinition](../BSplineCurveDefinition/BSplineCurveDefinition.md) ) As [BSplineCurve](../BSplineCurve/BSplineCurve.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [BSplineCurveDefinition](../BSplineCurveDefinition/BSplineCurveDefinition.md) | Input BSplineCurveDefinition object that defines the BSpline curve. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |