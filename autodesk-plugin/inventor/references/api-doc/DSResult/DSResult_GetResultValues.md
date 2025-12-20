# DSResult.GetResultValues Method

Parent Object: [DSResult](../DSResult/DSResult.md)

## Description

Returns an array representing the values for this result. The array consists of time-value pairs. The unit type of the value will vary depending on the type of value this result represents. For example, getting the extent length will be a distance and is always expressed in the database length unit of centimeters.

Results are available when the entire simulation has been computed (LastComputedTimeStep equals NumberOfTimeSteps).

## Syntax

DSResult.**GetResultValues**( ***ResultValues***() As Double )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ResultValues | Double | Output array of Doubles that consist of time-value pairs. |

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |