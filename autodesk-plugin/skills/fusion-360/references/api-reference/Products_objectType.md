# Products.objectType Property

Parent Object: [Products](Products.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Products.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"products\_var" is a variable referencing a Products object.  ```` ``` # Get the value of the property. propertyValue = products_var.objectType ``` ```` |

"products\_var" is a variable referencing a Products object. ```` ``` #include <Core/Application/Products.h>  // Get the value of the property. string propertyValue = products_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |