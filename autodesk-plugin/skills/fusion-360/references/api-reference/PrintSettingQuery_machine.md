# PrintSettingQuery.machine Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

The machine specifies which machine the found print setting are compatible with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. Ptr<Machine> propertyValue = printSettingQuery_var->machine();  // Set the value of the property, where value_var is a Machine. bool returnValue = printSettingQuery_var->machine(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Machine](Machine.htm).

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |