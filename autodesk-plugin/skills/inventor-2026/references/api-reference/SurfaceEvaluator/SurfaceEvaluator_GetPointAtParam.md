# SurfaceEvaluator.GetPointAtParam Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Calculates the coordinate points at the given parameter values on the surface.

## Syntax

SurfaceEvaluator.**GetPointAtParam**( ***Params***() As Double, ***Points***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Params | Double | Input/output array of Doubles that specifies the u-v parameters. The array is a single dimension array containing sequential u and v values. |
| Points | Double | Input/output double that specifies the points. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |

## Version

Introduced in version 4
