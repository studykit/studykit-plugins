# FavoriteMaterials.isValid Property

Parent Object: [FavoriteMaterials](FavoriteMaterials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteMaterials.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteMaterials\_var" is a variable referencing a FavoriteMaterials object. |

"favoriteMaterials\_var" is a variable referencing a FavoriteMaterials object. ```` ``` #include <Core/Materials/FavoriteMaterials.h>  // Get the value of the property. boolean propertyValue = favoriteMaterials_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |