# CAMAdditiveBuildExportFilter.objectType Property

Parent Object: [CAMAdditiveBuildExportFilter](CAMAdditiveBuildExportFilter.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/CAMAdditiveBuildExportFilter.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cAMAdditiveBuildExportFilter\_var" is a variable referencing a CAMAdditiveBuildExportFilter object.  ```` ``` # Get the value of the property. propertyValue = cAMAdditiveBuildExportFilter_var.objectType ``` ```` |

"cAMAdditiveBuildExportFilter\_var" is a variable referencing a CAMAdditiveBuildExportFilter object. ```` ``` #include <Cam/CAM/CAMAdditiveBuildExportFilter.h>  // Get the value of the property. string propertyValue = cAMAdditiveBuildExportFilter_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |