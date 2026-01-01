# DataProject.objectType Property

Parent Object: [DataProject](DataProject.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProject.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProject\_var" is a variable referencing a DataProject object.  ```` ``` # Get the value of the property. propertyValue = dataProject_var.objectType ``` ```` |

"dataProject\_var" is a variable referencing a DataProject object. ```` ``` #include <Core/Dashboard/DataProject.h>  // Get the value of the property. string propertyValue = dataProject_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |