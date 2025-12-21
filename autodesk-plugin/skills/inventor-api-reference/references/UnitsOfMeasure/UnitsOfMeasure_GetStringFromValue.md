# UnitsOfMeasure.GetStringFromValue Method

Parent Object: [UnitsOfMeasure](../UnitsOfMeasure/UnitsOfMeasure.md)

## Description

Method that creates a string that represents the input value evaluated using the specified units.

## Remarks

The input value is always in database units. The units can be defined using one the predefined units in the UnitTypeEnum enum or you can define your own unit type by combining known units in a string. You can also use the default unit types, (kDefaultDisplayLengthUnits, kDefaultDisplayAngleUnits, kDefaultDisplayMassUnits, kDefaultDisplayTimeUnits, or kDefaultDisplayTemperatureUnits), to use the current unit type defined in the document. For example, if the current length unit of the document is Inches and the precision for the length units is 3 decimal places, inputting 25.0 for the value and kDefaultDisplayLengthUnits for the units specifier will return the string '9.843 in'. This method fails when the value cannot be evaluated using the specified units specifier. This method is currently not supported when the UnitsOfMeasure object was obtained using Apprentice. A common use of this method will be to evaluate a value using the current display units of the document. For \example if the value defines a length you can use kDefaultDisplayLengthUnits as the unit specifier so the value will be evaluated as a length in the current document units. The enum values that specify to use the document default display units are kDefaultDisplayLengthUnits, kDefaultDisplayAngleUnits, kDefaultDisplayMassUnits, kDefaultDisplayTimeUnits, and kDefaultDisplayTemperatureUnits.

## Syntax

UnitsOfMeasure.**GetStringFromValue**( ***Value*** As Double, ***UnitsSpecifier*** As Variant ) As String

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Value | Double | Input Double value that contains the value in database units for the unit category specified in the second argument. |
| UnitsSpecifier | Variant | Input variant value that specifies the unit type the string is to be returned in. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". string specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 4
