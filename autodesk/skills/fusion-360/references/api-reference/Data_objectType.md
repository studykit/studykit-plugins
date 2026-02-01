# Data.objectType Property

Parent Object: [Data](Data.htm)
Defined in namespace "adsk::core" and the header file is <Core/Dashboard/Data.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"data\_var" is a variable referencing a Data object.  ```` ``` # Get the value of the property. propertyValue = data_var.objectType ``` ```` |

"data\_var" is a variable referencing a Data object. ```` ``` #include <Core/Dashboard/Data.h>  // Get the value of the property. string propertyValue = data_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version January 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |