# UnitsOfMeasure.GetDatabaseUnitsFromExpression Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Evaluates an input string and returns equivalent database units as a string.

## Syntax

UnitsOfMeasure.**GetDatabaseUnitsFromExpression**( ***Expression*** As String, ***UnitsSpecifier*** As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression | String | Input String value that contains the expression to evaluate. This string is evaluated the same ways a string entered in any of the Autodesk Inventor dialogs are evaluated. For example "3 in / 2 cm" is a valid string for input. |
| UnitsSpecifier | Variant | Input Variant value that specifies the unit type of the input value. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |