# SMTExportOptions.objectType Property

Parent Object: [SMTExportOptions](SMTExportOptions.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SMTExportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object.  ```` ``` # Get the value of the property. propertyValue = sMTExportOptions_var.objectType ``` ```` |

"sMTExportOptions\_var" is a variable referencing a SMTExportOptions object. ```` ``` #include <Fusion/Fusion/SMTExportOptions.h>  // Get the value of the property. string propertyValue = sMTExportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |