# TransientGeometry.CreateArc3dByThreePoints Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new Arc2d object by three points. The object created is a transient mathematical object and is not displayed graphically.

## Syntax

TransientGeometry.**CreateArc3dByThreePoints**( ***PointOne*** As [Point](../Point/Point.md), ***PointTwo*** As [Point](../Point/Point.md), ***PointThree*** As [Point](../Point/Point.md) ) As [Arc3d](../Arc3d/Arc3d.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PointOne | [Point](../Point/Point.md) | First of three points. |
| PointTwo | [Point](../Point/Point.md) | Second of three points. |
| PointThree | [Point](../Point/Point.md) | Third of three points. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2008
