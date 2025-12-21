# SurfaceEvaluator.GetNormalAtPoint Method

Parent Object: [SurfaceEvaluator](../SurfaceEvaluator/SurfaceEvaluator.md)

## Description

Function that returns the normal vectors for the specified points.

## Syntax

SurfaceEvaluator.**GetNormalAtPoint**( ***Points***() As Double, ***Normals***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Points | Double | Input Double array that specifies the x,y,z values of the point(s) to calculate the normal vector(s) for. The array consists of x,y,z values where each triplet defines a point in the model space of the surface. The points specified must lie on the surface. |
| Normals | Double | Output Double array that contains the x,y,z components of the normal vector(s). A triplet containing the x,y,z components of each vector is returned for each input point.  If an input point did not lie on the surface and a normal could not be computed, a zero length vector is returned. |

## Version

Introduced in version 2013
