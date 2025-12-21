# BSplineCurve.Split Method

Parent Object: [BSplineCurve](../BSplineCurve/BSplineCurve.md)

## Description

Creates two new curves that are the result of splitting this curve at the specified point. The original curve is left unchanged.

## Syntax

BSplineCurve.**Split**( ***SplitParam*** As Double, ***CurveOne*** As [BSplineCurve](../BSplineCurve/BSplineCurve.md), ***CurveTwo*** As [BSplineCurve](../BSplineCurve/BSplineCurve.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SplitParam | Double | Input Double that specifies the parameter where the curve is to be split. |
| CurveOne | [BSplineCurve](../BSplineCurve/BSplineCurve.md) | Output BSplineCurve that is the portion of the curve from the start of the curve to the split parameter location. |
| CurveTwo | [BSplineCurve](../BSplineCurve/BSplineCurve.md) | Output BSplineCurve that is the portion of the curve from the split parameter location to the end of the curve. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |