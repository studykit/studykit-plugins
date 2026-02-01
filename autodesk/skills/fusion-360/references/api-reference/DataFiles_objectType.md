# DataFiles.objectType Property

Parent Object: [DataFiles](DataFiles.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFiles.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFiles\_var" is a variable referencing a DataFiles object.  ```` ``` # Get the value of the property. propertyValue = dataFiles_var.objectType ``` ```` |

"dataFiles\_var" is a variable referencing a DataFiles object. ```` ``` #include <Core/Dashboard/DataFiles.h>  // Get the value of the property. string propertyValue = dataFiles_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |