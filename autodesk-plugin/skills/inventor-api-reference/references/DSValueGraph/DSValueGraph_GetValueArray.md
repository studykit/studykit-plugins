# DSValueGraph.GetValueArray Method

Parent Object: [DSValueGraph](../DSValueGraph/DSValueGraph.md)

## Description

Gets the values in the graph. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents.

## Syntax

DSValueGraph.**GetValueArray**( ***TimeValueArray***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| TimeValueArray | Double | Output Double array that contains the time-value pairs. The first value (x) is the time in seconds and should be a value within the range of the simulation. The second value (y) is the value for whatever is being defined. The units for this value depend on what is being set. For example, setting the velocity of a linear motion is always expressed in the database length unit of centimeters and the time unit of seconds. |

## Version

Introduced in version 2013
