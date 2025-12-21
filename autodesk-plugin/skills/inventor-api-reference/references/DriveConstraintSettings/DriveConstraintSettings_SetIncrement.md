# DriveConstraintSettings.SetIncrement Method

Parent Object: [DriveConstraintSettings](../DriveConstraintSettings/DriveConstraintSettings.md)

## Description

Sets the increment type and the value.

## Syntax

DriveConstraintSettings.**SetIncrement**( ***IncrementType*** As [ConstraintIncrementTypeEnum](ConstraintIncrementTypeEnum.md), ***Increment*** As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| IncrementType | [ConstraintIncrementTypeEnum](ConstraintIncrementTypeEnum.md) | Input enum that specifies the increment type. Valid values are kIncrementAsAmountOfValue and kIncrementAsNumberOfSteps. |
| Increment | String | Input String that specifies the increment value. The value is interpreted based on the increment type - amount of value if the type is kIncrementAsAmountOfValue and total number of steps if the type is kIncrementAsNumberOfSteps. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |