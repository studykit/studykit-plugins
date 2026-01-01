# PrintSetting.id Property

Parent Object: [PrintSetting](PrintSetting.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/PrintSetting/PrintSetting.h>

## Description

Gets the unique identifier of the PrintSetting. Can be used for comparing PrintSettings within the document.

## Syntax

* [Python](#Python)
* [C++](#C++)

"printSetting\_var" is a variable referencing a PrintSetting object. |

"printSetting\_var" is a variable referencing a PrintSetting object. ```` ``` #include <Cam/PrintSetting/PrintSetting.h>  // Get the value of the property. string propertyValue = printSetting_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |