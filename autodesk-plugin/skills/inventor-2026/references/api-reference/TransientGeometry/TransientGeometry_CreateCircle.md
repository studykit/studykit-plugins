# TransientGeometry.CreateCircle Method

Parent Object: [TransientGeometry](../TransientGeometry/TransientGeometry.md)

## Description

Method that creates a new 3d Circle object. The object created is a transient mathematical object and is not displayed graphically

## Syntax

TransientGeometry.**CreateCircle**( ***Center*** As [Point](../Point/Point.md), ***Normal*** As [UnitVector](../UnitVector/UnitVector.md), ***Radius*** As Double ) As [Circle](../Circle/Circle.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Center | [Point](../Point/Point.md) | Input Point object that specifies the center of the arc. |
| Normal | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector that specifies the axis of the circle. |
| Radius | Double | Input Double that specifies the radius of the circle. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 4
