# FavoriteAppearances.item Method

Parent Object: [FavoriteAppearances](FavoriteAppearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

Returns the specified Appearance using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object.```` ``` returnValue = favoriteAppearances_var.item(index) ``` ```` |

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Appearance](Appearance.htm) | Returns the specified appearance or null if an invalid index is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the appearance to return where the first item in the collection is 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |