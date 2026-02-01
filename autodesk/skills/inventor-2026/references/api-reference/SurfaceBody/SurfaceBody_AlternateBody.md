# SurfaceBody.AlternateBody Property

Parent Object: [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Description

Property that returns a new SurfaceBody that was derived from the existing body using the specified form input. The primary purpose of this property is to obtain a body that consists entirely of NURBS surfaces.

## Remarks

Valid values for the AlternateForm parameter are in the SurfaceGeometryFormEnum and are: \* SurfaceGeometryForm\_NURBS " Convert analytic surfaces to NURBS. This may result in splitting faces and edges as necessary. When used alone, only the faces are converted to NURBS. Edges will be represented by analytic curves. \* SurfaceGeometryForm\_ProceduralToNURBS " Convert procedural surfaces to more accurate NURB approximations. This may result in splitting faces and edges as necessary These are bitwise values and combining SurfaceGeometryForm\_NURBS and SurfaceGeometryForm\_ProceduralToNURBS will create a result where the entire body or face is converted to NURBS, procedural surfaces are accurately approximated, and all edges will also be converted to NURBS.

## Syntax

SurfaceBody.**AlternateBody**( ***AlternateForm*** As Long ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Property Value

This is a read only property whose value is a [SurfaceBody](../SurfaceBody/SurfaceBody.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| AlternateForm | Long | AlternateForm \- Input Long that is the sum of values describing the desired form. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Body Imprinting and matching the results](../../sample-programs/ImprintingAndMatching_Sample.md) | This sample is intended to demonstrate a technique of finding the matching surfaces between the original input bodies and output imprinted bodies. This relies on transient keys, which is a unique ID associated with each B-Rep entity. A transient key is only good as long as the model is not recomputed. |

## Version

Introduced in version 4
