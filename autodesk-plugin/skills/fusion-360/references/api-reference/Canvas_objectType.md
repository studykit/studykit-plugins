# Canvas.objectType Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object.  ```` ``` # Get the value of the property. propertyValue = canvas_var.objectType ``` ```` |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. string propertyValue = canvas_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |