# CAMExportOptions.objectType Property

Parent Object: [CAMExportOptions](CAMExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object.  ```` ``` # Get the value of the property. propertyValue = cAMExportOptions_var.objectType ``` ```` |

"cAMExportOptions\_var" is a variable referencing a CAMExportOptions object. ```` ``` #include <Cam/CAM/CAMExportOptions.h>  // Get the value of the property. string propertyValue = cAMExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |