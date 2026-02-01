# DataObjectFuture.objectType Property

Parent Object: [DataObjectFuture](DataObjectFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataObjectFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object.  ```` ``` # Get the value of the property. propertyValue = dataObjectFuture_var.objectType ``` ```` |

"dataObjectFuture\_var" is a variable referencing a DataObjectFuture object. ```` ``` #include <Core/Dashboard/DataObjectFuture.h>  // Get the value of the property. string propertyValue = dataObjectFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |