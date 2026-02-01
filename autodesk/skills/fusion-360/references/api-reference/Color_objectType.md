# Color.objectType Property

Parent Object: [Color](Color.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Color.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"color\_var" is a variable referencing a Color object.  ```` ``` # Get the value of the property. propertyValue = color_var.objectType ``` ```` |

"color\_var" is a variable referencing a Color object. ```` ``` #include <Core/Application/Color.h>  // Get the value of the property. string propertyValue = color_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |