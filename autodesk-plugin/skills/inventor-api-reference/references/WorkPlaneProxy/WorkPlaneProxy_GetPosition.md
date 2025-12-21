# WorkPlaneProxy.GetPosition Method

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Method that returns the position and orientation of a work plane. When sketches are created on a work plane they inherit the work plane's origin and orientation. This method is useful to predetermine what the orientation will be before the sketch is created.

## Syntax

WorkPlaneProxy.**GetPosition**( ***Origin*** As [Point](../Point/Point.md), ***XAxis*** As [UnitVector](../UnitVector/UnitVector.md), ***YAxis*** As [UnitVector](../UnitVector/UnitVector.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Origin | [Point](../Point/Point.md) | Output Point object that defines the origin of the work plane. |
| XAxis | [UnitVector](../UnitVector/UnitVector.md) | Output UnitVector object that defines the X-axis vector of the work plane. |
| YAxis | [UnitVector](../UnitVector/UnitVector.md) | Output UnitVector object that defines the Y-axis vector of the work plane. |

## Version

Introduced in version 5
