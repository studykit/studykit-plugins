# DataFileFuture.objectType Property

Parent Object: [DataFileFuture](DataFileFuture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/DataFileFuture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"dataFileFuture\_var" is a variable referencing a DataFileFuture object.  ```` ``` # Get the value of the property. propertyValue = dataFileFuture_var.objectType ``` ```` |

"dataFileFuture\_var" is a variable referencing a DataFileFuture object. ```` ``` #include <Core/Dashboard/DataFileFuture.h>  // Get the value of the property. string propertyValue = dataFileFuture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |