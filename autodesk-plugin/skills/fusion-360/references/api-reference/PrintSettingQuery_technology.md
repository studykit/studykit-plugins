# PrintSettingQuery.technology Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

The case-insensitive technology specifies technology of the PrintSetting.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. string propertyValue = printSettingQuery_var->technology();  // Set the value of the property, where value_var is a string. bool returnValue = printSettingQuery_var->technology(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |