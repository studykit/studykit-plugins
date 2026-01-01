# FavoriteAppearances.objectType Property

Parent Object: [FavoriteAppearances](FavoriteAppearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteAppearances\_var" is a variable referencing a FavoriteAppearances object.  ```` ``` # Get the value of the property. propertyValue = favoriteAppearances_var.objectType ``` ```` |

"favoriteAppearances\_var" is a variable referencing a FavoriteAppearances object. ```` ``` #include <Core/Materials/FavoriteAppearances.h>  // Get the value of the property. string propertyValue = favoriteAppearances_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |