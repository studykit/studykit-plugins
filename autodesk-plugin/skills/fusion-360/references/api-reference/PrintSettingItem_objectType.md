# PrintSettingItem.objectType Property

Parent Object: [PrintSettingItem](PrintSettingItem.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingItem.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingItem\_var" is a variable referencing a PrintSettingItem object.  ```` ``` # Get the value of the property. propertyValue = printSettingItem_var.objectType ``` ```` |

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. ```` ``` #include <Cam/PrintSetting/PrintSettingItem.h>  // Get the value of the property. string propertyValue = printSettingItem_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |