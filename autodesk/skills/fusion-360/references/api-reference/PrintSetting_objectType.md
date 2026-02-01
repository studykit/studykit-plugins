# PrintSetting.objectType Property

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a PrintSetting object.  ```` ``` # Get the value of the property. propertyValue = printSetting_var.objectType ``` ```` |

"printSetting\_var" is a variable referencing a PrintSetting object. ```` ``` #include <Cam/PrintSetting/PrintSetting.h>  // Get the value of the property. string propertyValue = printSetting_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |