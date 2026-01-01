# PrintSettingQuery.isValid Property

Parent Object: [PrintSettingQuery](PrintSettingQuery.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingQuery.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. |

"printSettingQuery\_var" is a variable referencing a PrintSettingQuery object. ```` ``` #include <Cam/PrintSetting/PrintSettingQuery.h>  // Get the value of the property. boolean propertyValue = printSettingQuery_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |