# PrintSettingQuery.filamentDiameter Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired. The machine now contains the filament diameter(s) in the extruder(s).

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object.  ```` ``` # Get the value of the property. propertyValue = printSettingQuery_var.filamentDiameter  # Set the value of the property. printSettingQuery_var.filamentDiameter = propertyValue ``` ```` |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. double propertyValue = printSettingQuery_var->filamentDiameter();  // Set the value of the property, where value_var is a double. bool returnValue = printSettingQuery_var->filamentDiameter(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023
Retired in version July 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |