# PrintSettingQuery.layerHeight Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

The layer height specifies layer height of the PrintSetting. This should match the PrintSetting layer height in cm.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. double propertyValue = printSettingQuery_var->layerHeight();  // Set the value of the property, where value_var is a double. bool returnValue = printSettingQuery_var->layerHeight(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |