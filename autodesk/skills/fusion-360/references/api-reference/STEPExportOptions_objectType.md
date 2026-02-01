# STEPExportOptions.objectType Property

Parent Object: [STEPExportOptions](STEPExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STEPExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTEPExportOptions\_var" is a variable referencing a STEPExportOptions object.  ```` ``` # Get the value of the property. propertyValue = sTEPExportOptions_var.objectType ``` ```` |

"sTEPExportOptions\_var" is a variable referencing a STEPExportOptions object. ```` ``` #include <Fusion/Fusion/STEPExportOptions.h>  // Get the value of the property. string propertyValue = sTEPExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |