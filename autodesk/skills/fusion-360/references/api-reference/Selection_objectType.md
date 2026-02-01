# Selection.objectType Property

Parent Object: [Selection](Selection.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selection\_var" is a variable referencing a Selection object.  ```` ``` # Get the value of the property. propertyValue = selection_var.objectType ``` ```` |

"selection\_var" is a variable referencing a Selection object. ```` ``` #include <Core/UserInterface/Selection.h>  // Get the value of the property. string propertyValue = selection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |