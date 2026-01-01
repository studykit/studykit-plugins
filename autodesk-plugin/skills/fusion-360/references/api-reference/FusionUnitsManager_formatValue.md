# FusionUnitsManager.formatValue Method

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

Given a floating point number this method evaluates it as a value of a specific unit type and returns an appropriate string. By default, the current unit settings defined in the user preferences is used, but you can set the method arguments to override the defaults to specify the formatting you want. The input value always uses internal units, which are centimeters for length, radians for angles, and mass is in kilograms.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.```` ``` # Uses no optional arguments. returnValue = fusionUnitsManager_var.formatValue(value)  # Uses optional arguments. returnValue = fusionUnitsManager_var.formatValue(value, units, precision, showTrailingZeros, minimumPrecision, showUnits) ``` ```` |

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.  ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Uses no optional arguments. returnValue = fusionUnitsManager_var->formatValue(value);  // Uses optional arguments. returnValue = fusionUnitsManager_var->formatValue(value, units, precision, showTrailingZeros, minimumPrecision, showUnits); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns the formatted string or an empty string in case of an error. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| value | double | A floating point value that is assumed to use the internal unit type, which are centimeters for length, radians for angles, and mass is in kilograms. |
| units | string | The units the value represents. The default value for this argument is "DefaultDistance" which means it will use the default distance units defined for the active design.   This is an optional argument whose default value is "DefaultDistance". |
| precision | integer | This specifies the number of decimal places to display. The default value is -1 which indicates the precision specified in preferences should be used. A maximum of 9 can be used and any larger numbers will be forced to 9.   This is an optional argument whose default value is -1. |
| showTrailingZeros | [BooleanOptions](BooleanOptions.htm) | Specifies if trailing zeros should be shown or not. The default value is to use the preference setting.   This is an optional argument whose default value is BooleanOptions.DefaultBooleanOption. |
| minimumPrecision | integer | When trailing zeros are not displayed, this specifies a minimum precision where some trailing zeros are still shown. The default value is -1 which indicates the minimum precision specified in preferences should be used. A maximum of 8 can be used, and any larger numbers will be forced to 8.   This is an optional argument whose default value is -1. |
| showUnits | boolean | This specifies whether the unit name or symbol should be included in the result.   This is an optional argument whose default value is True. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |