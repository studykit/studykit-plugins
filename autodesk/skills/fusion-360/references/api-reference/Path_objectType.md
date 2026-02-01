# Path.objectType Property

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"path\_var" is a variable referencing a Path object.  ```` ``` # Get the value of the property. propertyValue = path_var.objectType ``` ```` |

"path\_var" is a variable referencing a Path object. ```` ``` #include <Fusion/Features/Path.h>  // Get the value of the property. string propertyValue = path_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |