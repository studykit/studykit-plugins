# CAMExportFuture.objectType Property

Parent Object: [CAMExportFuture](CAMExportFuture.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMExportFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object.  ```` ``` # Get the value of the property. propertyValue = cAMExportFuture_var.objectType ``` ```` |

"cAMExportFuture\_var" is a variable referencing a CAMExportFuture object. ```` ``` #include <Cam/CAM/CAMExportFuture.h>  // Get the value of the property. string propertyValue = cAMExportFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |