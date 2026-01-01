# SATImportOptions.objectType Property

Parent Object: [SATImportOptions](SATImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SATImportOptions.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sATImportOptions\_var" is a variable referencing a SATImportOptions object.  ```` ``` # Get the value of the property. propertyValue = sATImportOptions_var.objectType ``` ```` |

"sATImportOptions\_var" is a variable referencing a SATImportOptions object. ```` ``` #include <Core/Application/SATImportOptions.h>  // Get the value of the property. string propertyValue = sATImportOptions_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |