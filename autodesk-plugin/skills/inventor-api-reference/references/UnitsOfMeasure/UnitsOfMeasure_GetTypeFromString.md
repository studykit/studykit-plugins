# UnitsOfMeasure.GetTypeFromString Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Given a string defining a unit this method returns the corresponding unit from the UnitsTypeEnum constant list. If the unit specified by the string does not exist in the constant list an error will occur. For example, inputting "mm" will return kMillimeterLengthUnits. This method is not currently supported when the UnitsOfMeasure object was obtained using Apprentice.

## Syntax

UnitsOfMeasure.**GetTypeFromString**( ***UnitsString*** As String ) As [UnitsTypeEnum](../UnitsTypeEnum.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UnitsString | String | Input string specifies the unit type. |

## Version

Introduced in version 4
