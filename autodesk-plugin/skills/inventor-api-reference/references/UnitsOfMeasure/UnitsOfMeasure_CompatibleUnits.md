# UnitsOfMeasure.CompatibleUnits Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Method that evaluates the two input expressions and determines if the result in units that have the same base unit type.

## Remarks

For example comparing the two expressions '3.45 in + 3 cm' and '1 ft' will return True because both expressions result in values that defined lengths. The two expression '3 cm \* 5 cm' and '1 ft' will return False because the first expression results in an area and the second is a length. This method will also return False in the case where either Expression1 or Expression2 is not valid and cannot be evaluated.

## Syntax

UnitsOfMeasure.**CompatibleUnits**( ***Expression1*** As String, ***UnitsSpecifier1*** As Variant, ***Expression2*** As String, ***UnitsSpecifier2*** As Variant ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Expression1 | String | The first expression to be used in the comparison. |
| UnitsSpecifier1 | Variant | Input variant value that specifies the unit type the first expression is to be evaluated with. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch\: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". A common use of this method will be to evaluate an expression using the current display units of the document. For example if the expression should define a length you can use kDefaultDisplayLengthUnit as the unit specifier so the expression will be evaluated as a length in the current document units. The enum values that specify to use the document default display units are kDefaultDisplayLengthUnit, kDefaultDisplayAngleUnit, kDefaultDisplayMassUnit, kDefaultDisplayTimeUnit, and kDefaultDisplayTemperatureUnit. |
| Expression2 | String | The second expression to be used in the comparison. |
| UnitsSpecifier2 | Variant | Input variant value that specifies the unit type the second expression is to be evaluated with. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch\: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". A common use of this method will be to evaluate an expression using the current display units of the document. For example if the expression should define a length you can use kDefaultDisplayLengthUnit as the unit specifier so the expression will be evaluated as a length in the current document units. The enum values that specify to use the document default display units are kDefaultDisplayLengthUnit, kDefaultDisplayAngleUnit, kDefaultDisplayMassUnit, kDefaultDisplayTimeUnit, and kDefaultDisplayTemperatureUnit. |

## Version

Introduced in version 8
