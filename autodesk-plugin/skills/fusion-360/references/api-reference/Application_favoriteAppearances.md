# Application.favoriteAppearances Property

Parent Object: [Application](Application.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Application.h>

## Description

Returns the set of favorite appearances.

## Syntax

* [Python](#Python)
* [C++](#C++)

"application\_var" is a variable referencing an Application object. |

"application\_var" is a variable referencing an Application object. ```` ``` #include <Core/Application/Application.h>  // Get the value of the property. Ptr<FavoriteAppearances> propertyValue = application_var->favoriteAppearances(); ``` ```` |

## Property Value

This is a read only property whose value is a [FavoriteAppearances](FavoriteAppearances.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |