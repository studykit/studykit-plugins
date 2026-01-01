# CAMExportManager.objectType Property

Parent Object: [CAMExportManager](CAMExportManager.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportManager.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportManager\_var" is a variable referencing a CAMExportManager object.  ```` ``` # Get the value of the property. propertyValue = cAMExportManager_var.objectType ``` ```` |

"cAMExportManager\_var" is a variable referencing a CAMExportManager object. ```` ``` #include <Cam/CAM/CAMExportManager.h>  // Get the value of the property. string propertyValue = cAMExportManager_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |