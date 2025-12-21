# UnitsOfMeasure.ConvertUnits Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Method that converts a value from one unit to another. The input and output unit specifiers must both define compatible units. For example, "in" (inches) and "cm" (centimeters) will work because they both define lengths. If incompatible units are specified, this method will fail. The converted value, in the units specified by the OutputUnitsSpecifier argument is returned.

## Syntax

UnitsOfMeasure.**ConvertUnits**( ***Value*** As Double, ***InputUnitsSpecifier*** As Variant, ***OutputUnitsSpecifier*** As Variant ) As Double

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Value | Double | Input Double value that specifies the value to be converted. This value is in the units specified by the InputUnitsSpecifier argument. |
| InputUnitsSpecifier | Variant | Input Variant value that specifies the unit type of the input value. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |
| OutputUnitsSpecifier | Variant | Input Variant value that specifies the unit type of the output value. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |

## Version

Introduced in version 8
