# PrintSetting.isValid Property

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a PrintSetting object. |

"printSetting\_var" is a variable referencing a PrintSetting object. ```` ``` #include <Cam/PrintSetting/PrintSetting.h>  // Get the value of the property. boolean propertyValue = printSetting_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |