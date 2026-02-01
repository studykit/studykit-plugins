# ProductPreferences.objectType Property

Parent Object: [ProductPreferences](ProductPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferences.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productPreferences\_var" is a variable referencing a ProductPreferences object.  ```` ``` # Get the value of the property. propertyValue = productPreferences_var.objectType ``` ```` |

"productPreferences\_var" is a variable referencing a ProductPreferences object. ```` ``` #include <Core/Application/ProductPreferences.h>  // Get the value of the property. string propertyValue = productPreferences_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |