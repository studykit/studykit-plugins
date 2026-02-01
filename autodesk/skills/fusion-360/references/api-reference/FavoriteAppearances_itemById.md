# FavoriteAppearances.itemById Method

Parent Object: [FavoriteAppearances](FavoriteAppearances.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteAppearances.h>

## Description

Returns the Appearance by it's internal unique ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object.```` ``` returnValue = favoriteAppearances_var.itemById(id) ``` ```` |

"favoriteAppearances\_var" is a variable referencing a [FavoriteAppearances](FavoriteAppearances.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Appearance](Appearance.htm) | Returns the specified appearance or null if there isn't a matching ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the appearance to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |