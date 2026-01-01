# SurfaceBodyProxy.IsEntityValid Method

Parent Object: [SurfaceBodyProxy](../SurfaceBodyProxy/SurfaceBodyProxy.md)

## Description

Method that returns whether an entity passes the quality check at the specified level.

## Syntax

SurfaceBodyProxy.**IsEntityValid**( [***EntityToCheck***] As Variant, [***CheckLevel***] As Long, [***ProblemEntities***] As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityToCheck | Variant | Method checks whole body if not specified. Valid inputs: FaceShell, Wire, Face, Edge and Vertex. |
| CheckLevel | Long | Value Checks Performed 1-Fast error checks. 2-As above plus slower error checks. 3-(default) As above plus D-cubed curve and surface checks. 4-As above plus fast warning checks. 5-As above plus slower warning checks. 6-As above plus slow edge convexity change point checks. 7-As above plus face/face intersection checks.   This is an optional argument whose default value is 3. |
| ProblemEntities | Variant | Output ObjectsEnumerator containing the entities that did not pass the check.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2009
