# TransientGeometry.CreateFittedBSplineCurve2d Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new object using fit points. The definition of the curve is supplied using the input definition object. If an invalid curve is defined the method will fail. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateFittedBSplineCurve2d**( ***Definition*** As [BSplineCurve2dDefinition](../BSplineCurve2dDefinition/BSplineCurve2dDefinition.md) ) As [BSplineCurve2d](../BSplineCurve2d/BSplineCurve2d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [BSplineCurve2dDefinition](../BSplineCurve2dDefinition/BSplineCurve2dDefinition.md) | Input BSplineCurve2dDefinition object that defines the 2d BSpline curve. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |