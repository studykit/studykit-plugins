# WorkAxes.AddFixed Method

Parent Object: [WorkAxes](../WorkAxes/WorkAxes.md)

## Description

Method that creates a new work axis that passes through the input point in the direction of the input vector. When used to create a work axis within an assembly the resulting work axis will return an AssemblyWorkAxisDef definition.

## Syntax

WorkAxes.**AddFixed**( ***Point*** As [Point](../Point/Point.md), ***Axis*** As [UnitVector](../UnitVector/UnitVector.md), [***Construction***] As Boolean ) As [WorkAxis](../WorkAxis/WorkAxis.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Point | [Point](../Point/Point.md) | Input  object. |
| Axis | [UnitVector](../UnitVector/UnitVector.md) | Input UnitVector object. that defines the X-axis vector of the work plane. |
| Construction | Boolean | Optional Input Boolean that specifies whether to create the work axis as a construction axis or not. The default is False, which indicates to create a standard work axis. A construction work axis is hidden from the user and is not displayed graphically or listed in the browser. |

## Version

Introduced in version 4
