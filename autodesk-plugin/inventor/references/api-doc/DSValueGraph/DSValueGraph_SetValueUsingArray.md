# DSValueGraph.SetValueUsingArray Method

Parent Object: [DSValueGraph](../DSValueGraph/DSValueGraph.md)

## Description

Sets the values in the graph. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents.

## Syntax

DSValueGraph.**SetValueUsingArray**( ***TimeValueArray***() As Double, [***InterpolationType***] As [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TimeValueArray | Double | Input Double array that contains the time-value pairs. The first value (x) is the time in seconds and should be a value within the range of the simulation. The second value (y) is the value for whatever is being defined. The units for this value depend on what is being set. For example, setting the velocity of a linear motion is always expressed in the database length unit of centimeters and the time unit of seconds. |
| InterpolationType | [DSGraphInterpolationTypeEnum](../DSGraphInterpolationTypeEnum.md) | Optional input that defines the type of interpolation to apply between each point when fitting the curve. This setting will be applied to the entire curve. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |