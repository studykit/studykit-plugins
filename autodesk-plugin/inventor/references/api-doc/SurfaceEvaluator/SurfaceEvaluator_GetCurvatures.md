# SurfaceEvaluator.GetCurvatures Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Calculates the curvature direction and magnitude of the curve at the given parameter values.

## Syntax

SurfaceEvaluator.**GetCurvatures**( ***Params***() As Double, ***MaxTangents***() As Double, ***MaxCurvatures***() As Double, ***MinCurvatures***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Params | Double | Input/output array of Doubles that specifies the parameters. |
| MaxTangents | Double | Output Double array that returns the maximum curvature direction vector at each specified parameter point. |
| MaxCurvatures | Double | Output Double array that returns the maximum curvature value at each specified parameter point. |
| MinCurvatures | Double | Output Double array that returns the minimum curvature value at each specified parameter point. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |