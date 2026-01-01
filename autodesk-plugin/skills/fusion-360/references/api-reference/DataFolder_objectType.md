# DataFolder.objectType Property

Parent Object: [DataFolder](DataFolder.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFolder.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFolder\_var" is a variable referencing a DataFolder object.  ```` ``` # Get the value of the property. propertyValue = dataFolder_var.objectType ``` ```` |

"dataFolder\_var" is a variable referencing a DataFolder object. ```` ``` #include <Core/Dashboard/DataFolder.h>  // Get the value of the property. string propertyValue = dataFolder_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |