# UnitsOfMeasure.GetPreciseStringFromValue Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Obtains the precise string along with the units, given a value. The output units needs to be specified as well.

## Syntax

UnitsOfMeasure.**GetPreciseStringFromValue**( ***Value*** As Double, ***UnitsSpecifier*** As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Value | Double | Value from which to obtain precise string and units. |
| UnitsSpecifier | Variant | Input variant value that specifies the unit type the string is to be returned in. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". string specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |