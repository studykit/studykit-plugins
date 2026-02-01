# FusionUnitsManager.formatInternalValue Method

Parent Object: [FusionUnitsManager](FusionUnitsManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/FusionUnitsManager.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been replaced by the formatValue method. This method does not honor the preferences for the precision, as it's supposed to. The formatValue method provides this capability and the ability to override the preference settings and specify how the value should be formatted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.```` ``` # Uses no optional arguments. returnValue = fusionUnitsManager_var.formatInternalValue(internalValue)  # Uses optional arguments. returnValue = fusionUnitsManager_var.formatInternalValue(internalValue, displayUnits, showUnits) ``` ```` |

"fusionUnitsManager\_var" is a variable referencing a [FusionUnitsManager](FusionUnitsManager.htm) object.  ```` ``` #include <Fusion/Fusion/FusionUnitsManager.h>  // Uses no optional arguments. returnValue = fusionUnitsManager_var->formatInternalValue(internalValue);  // Uses optional arguments. returnValue = fusionUnitsManager_var->formatInternalValue(internalValue, displayUnits, showUnits); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| string | Returns an empty string if the units are incorrectly specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| internalValue | double | The internal value to format. |
| displayUnits | string | The units to display the value in. If not supplied the units will default to the default length specified in the preferences.   This is an optional argument whose default value is "DefaultDistance". |
| showUnits | boolean | Specify false to exclude units from the format. The default is true.   This is an optional argument whose default value is True. |

## Version

Introduced in version August 2014
Retired in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |