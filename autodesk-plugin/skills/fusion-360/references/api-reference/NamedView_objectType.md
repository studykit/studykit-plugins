# NamedView.objectType Property

Parent Object: [NamedView](NamedView.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedView.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedView\_var" is a variable referencing a NamedView object.  ```` ``` # Get the value of the property. propertyValue = namedView_var.objectType ``` ```` |

"namedView\_var" is a variable referencing a NamedView object. ```` ``` #include <Core/Application/NamedView.h>  // Get the value of the property. string propertyValue = namedView_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |