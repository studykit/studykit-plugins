# DriveSettings.GetIncrement Method

Parent Object: [DriveSettings](../DriveSettings/DriveSettings.md)

## Description

Method that returns how the increment was specified and the value.

## Syntax

DriveSettings.**GetIncrement**( ***IncrementType*** As [IncrementTypeEnum](../IncrementTypeEnum.md), ***Increment*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IncrementType | [IncrementTypeEnum](../IncrementTypeEnum.md) | Output enum that returns the increment type. The possible return values are kIncrementAsAmountOfValue and kIncrementAsNumberOfSteps. |
| Increment | String | Output String that returns the increment value. The value returned is based on the increment type - amount of value if the type is kIncrementAsAmountOfValue and total number of steps if the type is kIncrementAsNumberOfSteps. |

## Version

Introduced in version 2014
