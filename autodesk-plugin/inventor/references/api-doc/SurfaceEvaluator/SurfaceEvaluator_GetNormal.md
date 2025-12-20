# SurfaceEvaluator.GetNormal Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Method that gets the surface normal.

## Syntax

SurfaceEvaluator.**GetNormal**( ***Params***() As Double, ***Normals***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Params | Double | Input/output array of Doubles that specifies the parameters. |
| Normals | Double | Input/output array of Doubles that contains the x-y-z values of the normals. The array is a single dimension array containing sequential x, y, and z values. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Is cylindrical face interior or exterior?](../../sample-programs/Line_IsColinearTo_Sample.md) | This sample shows how to determine whether the selected cylindircal face is an exterior face or an interior (hollow) face. |
| [Tapered Surface Using Offset Curve and Ruled Surface](../../sample-programs/TaperFace_Sample.md) | This sample demonstrates much of the wire body creation functionality. To run the sample you must have a part open and select a planar face. This sample then creates a trasient wire body using the geometry of the outside of the selected face. It then transforms and offsets that wire, and finally creates a ruled surface between the original wire and the offset wire. A base feature is created with the ruled surface. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |