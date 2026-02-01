# FavoriteAppearances.itemByName Method

Parent Object: [FavoriteAppearances](FavoriteAppearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

Returns the specified appearance using the name as seen in the user interface. This often isn't a reliable way of accessing a specific appearance because appearances are not required to be unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object.```` ``` returnValue = favoriteAppearances_var.itemByName(name) ``` ```` |

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Appearance](Appearance.htm) | Returns the specified appearance or null if there isn't a matching name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the appearance to return,. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |