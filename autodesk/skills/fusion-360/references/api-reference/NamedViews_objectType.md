# NamedViews.objectType Property

Parent Object: [NamedViews](NamedViews.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedViews.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedViews\_var" is a variable referencing a NamedViews object.  ```` ``` # Get the value of the property. propertyValue = namedViews_var.objectType ``` ```` |

"namedViews\_var" is a variable referencing a NamedViews object. ```` ``` #include <Core/Application/NamedViews.h>  // Get the value of the property. string propertyValue = namedViews_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |