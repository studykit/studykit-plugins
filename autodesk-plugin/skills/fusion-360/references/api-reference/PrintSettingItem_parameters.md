# PrintSettingItem.parameters Property

Parent Object: [PrintSettingItem](PrintSettingItem.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSettingItem.h>

## Description

Function that returns the parameters for reading and editing values.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. |

"printSettingItem\_var" is a variable referencing a PrintSettingItem object. ```` ``` #include <Cam/PrintSetting/PrintSettingItem.h>  // Get the value of the property. Ptr<CAMParameters> propertyValue = printSettingItem_var->parameters(); ``` ```` |

## Property Value

This is a read only property whose value is a [CAMParameters](CAMParameters.htm).

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |