# SurfaceEvaluator.GetParamAnomaly Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Gets general information about the parameterization of the surface, such as whether or not it is periodic, singular, or unbounded in the parameter domain.

## Syntax

SurfaceEvaluator.**GetParamAnomaly**( ***PeriodicityU***() As Double, ***PeriodicityV***() As Double, ***NumEndSingularitiesU*** As Long, ***SingularitiesU***() As Double, ***NumEndSingularitiesV*** As Long, ***SingularitiesV***() As Double, ***UnboundedParams***() As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PeriodicityU | Double | Output two element Double array that returns whether the surface is periodic in the U parameter direction. If the surface is periodic in U, the first array element is the period of the surface in U and the second element is the starting U parameter of the principle period. If the surface is not periodic in U, the first element is zero, and the second element is unused. |
| PeriodicityV | Double | Output two element Double array that returns whether the surface is periodic in the V parameter direction. If the surface is periodic in V, the first array element is the period of the surface in V and the second element is the starting V parameter of the principle period. If the surface is not periodic in V, the first element is zero, and the second element is unused. |
| NumEndSingularitiesU | Long | Output Double that returns the number of singularities in the U parameter direction. Valid values are zero to indicate no singularities, one to indicate one end singularity, or two to indicate a singularity at both ends. |
| SingularitiesU | Double | Output Double array that returns the U parameter values at which there is a singularity. If NumEndSingularitiesU returns zero, this argument is not used. |
| NumEndSingularitiesV | Long | Output Double that returns the number of singularities in the V parameter direction. Valid values are zero to indicate no singularities, one to indicate one end singularity, or two to indicate a singularity at both ends. |
| SingularitiesV | Double | Output Double array that returns the V parameter values at which there is a singularity. If NumEndSingularitiesV returns zero, this argument is not used. |
| UnboundedParams | Boolean | Input/output Boolean array of two elements that returns whether the surface is unbounded in the U or V parameter directions. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |