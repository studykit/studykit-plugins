# SMTImportOptions.objectType Property

Parent Object: [SMTImportOptions](SMTImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SMTImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sMTImportOptions\_var" is a variable referencing a SMTImportOptions object.  ```` ``` # Get the value of the property. propertyValue = sMTImportOptions_var.objectType ``` ```` |

"sMTImportOptions\_var" is a variable referencing a SMTImportOptions object. ```` ``` #include <Core/Application/SMTImportOptions.h>  // Get the value of the property. string propertyValue = sMTImportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |