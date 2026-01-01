# NamedValues.objectType Property

Parent Object: [NamedValues](NamedValues.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/NamedValues.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"namedValues\_var" is a variable referencing a NamedValues object.  ```` ``` # Get the value of the property. propertyValue = namedValues_var.objectType ``` ```` |

"namedValues\_var" is a variable referencing a NamedValues object. ```` ``` #include <Core/Application/NamedValues.h>  // Get the value of the property. string propertyValue = namedValues_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |