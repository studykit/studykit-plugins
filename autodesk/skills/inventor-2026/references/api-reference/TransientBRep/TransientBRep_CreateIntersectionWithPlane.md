# TransientBRep.CreateIntersectionWithPlane Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that intersects a body with a plane.

## Remarks

The returned SurfaceBody is a wire body that contains the intersection curves.

## Syntax

TransientBRep.**CreateIntersectionWithPlane**( ***Body*** As [SurfaceBody](../SurfaceBody/SurfaceBody.md), ***Plane*** As [Plane](../Plane/Plane.md) ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Body | [SurfaceBody](../SurfaceBody/SurfaceBody.md) | Input SurfaceBody to intersect. |
| Plane | [Plane](../Plane/Plane.md) | Input Plane that defines the plane to intersect the body with. |

## Version

Introduced in version 2009
