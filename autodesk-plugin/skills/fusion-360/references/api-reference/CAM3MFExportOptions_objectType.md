# CAM3MFExportOptions.objectType Property

Parent Object: [CAM3MFExportOptions](CAM3MFExportOptions.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAM3MFExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object.  ```` ``` # Get the value of the property. propertyValue = cAM3MFExportOptions_var.objectType ``` ```` |

"cAM3MFExportOptions\_var" is a variable referencing a CAM3MFExportOptions object. ```` ``` #include <Cam/CAM/CAM3MFExportOptions.h>  // Get the value of the property. string propertyValue = cAM3MFExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |