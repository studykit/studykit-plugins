# DataProjects.objectType Property

Parent Object: [DataProjects](DataProjects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataProjects.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataProjects\_var" is a variable referencing a DataProjects object.  ```` ``` # Get the value of the property. propertyValue = dataProjects_var.objectType ``` ```` |

"dataProjects\_var" is a variable referencing a DataProjects object. ```` ``` #include <Core/Dashboard/DataProjects.h>  // Get the value of the property. string propertyValue = dataProjects_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |