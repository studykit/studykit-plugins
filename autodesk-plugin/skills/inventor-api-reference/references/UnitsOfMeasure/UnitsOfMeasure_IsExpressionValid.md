# UnitsOfMeasure.IsExpressionValid Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Returns whether the input expression is valid or not.

## Syntax

UnitsOfMeasure.**IsExpressionValid**( ***Expression*** As String, ***UnitsSpecifier*** As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression | String | Input String value that specifies the equation. This string is evaluated the same way as strings entered in any of the Inventor dialogs are evaluated. For example '3 in + 2 cm' is a valid string for input. |
| UnitsSpecifier | Variant | Input value that specifies the type of unit the expression should be evaluated. The units can be specified using either a string defining a valid unit or an item from the UnitsTypeEnum. If the expression does specify a unit type, it should match the unit type specified by the UnitsSpecifier, otherwise an error will occur. |

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |