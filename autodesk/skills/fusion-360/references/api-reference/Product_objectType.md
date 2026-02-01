# Product.objectType Property

Parent Object: [Product](Product.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Product.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"product\_var" is a variable referencing a Product object.  ```` ``` # Get the value of the property. propertyValue = product_var.objectType ``` ```` |

"product\_var" is a variable referencing a Product object. ```` ``` #include <Core/Application/Product.h>  // Get the value of the property. string propertyValue = product_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |