# TransientBRep.CreateSolidTorus Method

Parent Object: [TransientBRep](../TransientBRep/TransientBRep.md)

## Description

Method that creates a solid torus.

## Remarks

The axis of the resulting torus is parallel to the model z-axis.

## Syntax

TransientBRep.**CreateSolidTorus**( ***Center*** As [Point](../Point/Point.md), ***MajorRadius*** As Double, ***MinorRadius*** As Double ) As [SurfaceBody](../SurfaceBody/SurfaceBody.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point](../Point/Point.md) | Input Point that defines the center of the torus. |
| MajorRadius | Double | Input Double that defines the major radius of the torus in centimeters. |
| MinorRadius | Double | Input Double that defines the minor radius of the torus in centimeters. |

## Version

Introduced in version 2009
