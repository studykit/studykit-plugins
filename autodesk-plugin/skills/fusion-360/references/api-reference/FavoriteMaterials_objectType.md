# FavoriteMaterials.objectType Property

Parent Object: [FavoriteMaterials](FavoriteMaterials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteMaterials.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteMaterials\_var" is a variable referencing a FavoriteMaterials object.  ```` ``` # Get the value of the property. propertyValue = favoriteMaterials_var.objectType ``` ```` |

"favoriteMaterials\_var" is a variable referencing a FavoriteMaterials object. ```` ``` #include <Core/Materials/FavoriteMaterials.h>  // Get the value of the property. string propertyValue = favoriteMaterials_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |