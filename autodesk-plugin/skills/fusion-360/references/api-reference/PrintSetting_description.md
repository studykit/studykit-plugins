# PrintSetting.description Property

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Gets and sets the description of the PrintSetting.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a PrintSetting object. |

"printSetting\_var" is a variable referencing a PrintSetting object. ```` ``` #include <Cam/PrintSetting/PrintSetting.h>  // Get the value of the property. string propertyValue = printSetting_var->description();  // Set the value of the property, where value_var is a string. bool returnValue = printSetting_var->description(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |