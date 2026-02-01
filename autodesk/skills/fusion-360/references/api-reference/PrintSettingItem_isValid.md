# PrintSettingItem.isValid Property

Parent Object: [PrintSettingItem](PrintSettingItem.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingItem.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. |

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. ```` ``` #include <Cam/PrintSetting/PrintSettingItem.h>  // Get the value of the property. boolean propertyValue = printSettingItem_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |