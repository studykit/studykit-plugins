# UnitsOfMeasure.GetValueFromExpression Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Method that evaluates the input expression using the units specified and returns a value in database units.

## Remarks

Example: the string "34 in / 2" with a length unit specifier, will return the value 43.1800. The UnitsSpecifier is used to determine the type of unit that is expected, (i.e.. area, volume, velocity, etc.) and is used for values that do not have an explicit type defined. For example the expression "4 \* 5" with a units specifier of "mm mm" would be assumed to be "4 mm \* 5 mm." An error occurs if the string cannot be evaluated. This method is currently not supported when the UnitsOfMeasure object was obtained using Apprentice. A common use of this method will be to evaluate an expression using the current display units of the document. For example if the expression should define a length you can use kDefaultDisplayLengthUnits as the unit specifier so the expression will be evaluated as a length in the current document units. The enum values that specify to use the document default display units are kDefaultDisplayLengthUnits, kDefaultDisplayAngleUnits, kDefaultDisplayMassUnits, kDefaultDisplayTimeUnits, and kDefaultDisplayTemperatureUnits. The input expression is specified by a string. This string may or may not specify a unit type (for example, "1" versus "1 in"). In the case where the string expression does not specify a unit type, the additional unit-type argument is required to determine the unit type. **Note:** Up to and including Autodesk Inventor 10, if the string expression does specify a unit type, the UnitsSpecifier type specified will be ignored because the unit type is obtained from the string expression. However, subsequent releases of Autodesk Inventor will return an error condition if the two unit types do not match.

## Syntax

UnitsOfMeasure.**GetValueFromExpression**( ***Expression*** As String, ***UnitsSpecifier*** As Variant ) As Variant

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression | String | Input String value that contains the expression to evaluate. This string is evaluated the same ways a string entered in any of the Autodesk Inventor dialogs are evaluated. For example "3 in / 2 cm" is a valid string for input. |
| UnitsSpecifier | Variant | Input variant value that specifies the unit type the expression is to be evaluated with. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in." String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in." |

## Version

Introduced in version 4
