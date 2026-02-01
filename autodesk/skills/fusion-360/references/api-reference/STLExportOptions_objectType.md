# STLExportOptions.objectType Property

Parent Object: [STLExportOptions](STLExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/STLExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object.  ```` ``` # Get the value of the property. propertyValue = sTLExportOptions_var.objectType ``` ```` |

"sTLExportOptions\_var" is a variable referencing a STLExportOptions object. ```` ``` #include <Fusion/Fusion/STLExportOptions.h>  // Get the value of the property. string propertyValue = sTLExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |