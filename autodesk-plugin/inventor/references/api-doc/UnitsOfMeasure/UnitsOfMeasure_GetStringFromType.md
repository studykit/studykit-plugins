# UnitsOfMeasure.GetStringFromType Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Given a unit type from the UnitsTypeEnum as input, this method returns the string that can be used to specify the same unit type.

## Remarks

For example if you input k kInchLengthUnits it will return the string "in." If one of the default unit types is specified, (kDefaultDisplayLengthUnits, kDefaultDisplayAngleUnits, kDefaultDisplayMassUnits, kDefaultDisplayTimeUnits, or kDefaultDisplayTemperatureUnits) this will return the string corresponding to the document default for that unit type. This method is currently not supported when the UnitsOfMeasure object was obtained using Apprentice.

## Syntax

UnitsOfMeasure.**GetStringFromType**( ***UnitsType*** As [UnitsTypeEnum](../UnitsTypeEnum.md) ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| UnitsType | [UnitsTypeEnum](../UnitsTypeEnum.md) | Input constant value that specifies the unit type. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |