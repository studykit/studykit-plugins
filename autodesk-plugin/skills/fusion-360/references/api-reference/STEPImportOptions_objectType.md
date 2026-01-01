# STEPImportOptions.objectType Property

Parent Object: [STEPImportOptions](STEPImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/STEPImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object.  ```` ``` # Get the value of the property. propertyValue = sTEPImportOptions_var.objectType ``` ```` |

"sTEPImportOptions\_var" is a variable referencing a STEPImportOptions object. ```` ``` #include <Core/Application/STEPImportOptions.h>  // Get the value of the property. string propertyValue = sTEPImportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |