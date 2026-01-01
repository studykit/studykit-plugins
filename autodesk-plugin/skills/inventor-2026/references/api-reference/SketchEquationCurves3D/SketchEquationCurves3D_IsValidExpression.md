# SketchEquationCurves3D.IsValidExpression Method

Parent Object: [SketchEquationCurves3D](../SketchEquationCurves3D/SketchEquationCurves3D.md)

## Description

Function that evaluates the provided expression and returns whether it is a valid expression or not. This can be useful when you allow the user to enter an expression and verify that it is valid before attempting to use it.

## Syntax

SketchEquationCurves3D.**IsValidExpression**( ***Expression*** As String, ***Unit*** As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression | String | Input String value that contains the expression to evaluate. |
| Unit | Variant | Input variant value that specifies the unit type the expression is to be evaluated with. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in." String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in” or “in^3”. |

## Version

Introduced in version 2014
