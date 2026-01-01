# ProductPreferencesCollection.objectType Property

Parent Object: [ProductPreferencesCollection](ProductPreferencesCollection.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ProductPreferencesCollection.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"productPreferencesCollection\_var" is a variable referencing a ProductPreferencesCollection object.  ```` ``` # Get the value of the property. propertyValue = productPreferencesCollection_var.objectType ``` ```` |

"productPreferencesCollection\_var" is a variable referencing a ProductPreferencesCollection object. ```` ``` #include <Core/Application/ProductPreferencesCollection.h>  // Get the value of the property. string propertyValue = productPreferencesCollection_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |