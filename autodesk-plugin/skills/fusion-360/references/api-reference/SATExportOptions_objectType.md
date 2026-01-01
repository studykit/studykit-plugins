# SATExportOptions.objectType Property

Parent Object: [SATExportOptions](SATExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SATExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sATExportOptions\_var" is a variable referencing a SATExportOptions object.  ```` ``` # Get the value of the property. propertyValue = sATExportOptions_var.objectType ``` ```` |

"sATExportOptions\_var" is a variable referencing a SATExportOptions object. ```` ``` #include <Fusion/Fusion/SATExportOptions.h>  // Get the value of the property. string propertyValue = sATExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |