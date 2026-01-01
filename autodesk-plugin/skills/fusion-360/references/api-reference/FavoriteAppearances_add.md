# FavoriteAppearances.add Method

Parent Object: [FavoriteAppearances](FavoriteAppearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

Adds an existing appearance to the Favorites list

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object.```` ``` returnValue = favoriteAppearances_var.add(appearance) ``` ```` |

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Appearance](Appearance.htm) | Returns the Appearance added to the favorites list or null if the operation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| appearance | [Appearance](Appearance.htm) | The appearance to be added to the favorites list. This can come from a Library or from a Design. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |