# ExportOptions.objectType Property

Parent Object: [ExportOptions](ExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"exportOptions\_var" is a variable referencing an ExportOptions object.  ```` ``` # Get the value of the property. propertyValue = exportOptions_var.objectType ``` ```` |

"exportOptions\_var" is a variable referencing an ExportOptions object. ```` ``` #include <Fusion/Fusion/ExportOptions.h>  // Get the value of the property. string propertyValue = exportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |