# UserParameters.AddByValue Method

Parent Object: [UserParameters](../UserParameters/UserParameters.md)

## Description

Method that creates a new parameter given a name and equation.

## Syntax

UserParameters.**AddByValue**( ***Name*** As String, ***Value*** As Variant, ***UnitsSpecifier*** As Variant ) As [UserParameter](../UserParameter/UserParameter.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String value that specifies the name for the parameter. The name must be unique with respect to all other parameters in this document. If a unique name is not specified an error will occur. |
| Value | Variant | Input Double value that specifies the value for the parameter. This value is given in database units for the unit type defined by the UnitType argument. |
| UnitsSpecifier | Variant | Input value that specifies the type of unit the parameter is. The units can be specified using either a string defining a valid unit or an item from the UnitsTypeEnum. If the equation references existing parameters, this unit type must be consistent with the unit type defined by the equation, otherwise an error will occur. You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For \example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create user parameters](../../sample-programs/ParameterCreateUser_Sample.md) | This sample demonstrates creating user parameters using an expression and a value. A part document must be open and it must not contain user parameters named "NewParam1" and "NewParam2". |
| [Text and Boolean user parameter creation](../../sample-programs/TextBooleanUserParameters_Sample.md) | This sample demonstrates how to create Text and Boolean user parameter. |

## Version

Introduced in version 4
