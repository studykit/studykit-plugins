# PrintSettingItem.name Property

Parent Object: [PrintSettingItem](PrintSettingItem.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingItem.h>

## Description

Body Preset get and set name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. |

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. ```` ``` #include <Cam/PrintSetting/PrintSettingItem.h>  // Get the value of the property. string propertyValue = printSettingItem_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = printSettingItem_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |