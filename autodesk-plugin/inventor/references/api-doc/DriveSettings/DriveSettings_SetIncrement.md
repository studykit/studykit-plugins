# DriveSettings.SetIncrement Method

Parent Object: [DriveSettings](../DriveSettings/DriveSettings.md)

## Description

Method that sets the increment type and the value.

## Syntax

DriveSettings.**SetIncrement**( ***IncrementType*** As [IncrementTypeEnum](../IncrementTypeEnum.md), ***Increment*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IncrementType | [IncrementTypeEnum](../IncrementTypeEnum.md) | Input enum that specifies the increment type. Valid values are kIncrementAsAmountOfValue and kIncrementAsNumberOfSteps. |
| Increment | String | Input String that specifies the increment value. The value is interpreted based on the increment type - amount of value if the type is kIncrementAsAmountOfValue and total number of steps if the type is kIncrementAsNumberOfSteps. |

## Version

Introduced in version 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |