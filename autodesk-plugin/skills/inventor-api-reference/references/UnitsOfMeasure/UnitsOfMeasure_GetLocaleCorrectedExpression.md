# UnitsOfMeasure.GetLocaleCorrectedExpression Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

This method converts the input expression to a locale-friendly version. For instance, if you input "1.0 in" on a machine set to the German locale, the return value is "1,0 in". In this case, the decimal separator is different.

## Syntax

UnitsOfMeasure.**GetLocaleCorrectedExpression**( ***Expression*** As String, ***UnitsSpecifier*** As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression | String | Input String value that contains the expression to evaluate. This string is evaluated the same ways a string entered in any of the Autodesk Inventor dialogs are evaluated. For example "3 in / 2 cm" is a valid string for input. |
| UnitsSpecifier | Variant | Input variant value that specifies the unit type the string is to be returned in. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and 'in'. string specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string 'in in in'. |

## Version

Introduced in version 10

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |