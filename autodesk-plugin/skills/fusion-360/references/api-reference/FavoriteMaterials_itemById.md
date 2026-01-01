# FavoriteMaterials.itemById Method

Parent Object: [FavoriteMaterials](FavoriteMaterials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteMaterials.h>

## Description

Returns the Material by it's internal unique ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteMaterials\_var" is a variable referencing a [FavoriteMaterials](FavoriteMaterials.htm) object.```` ``` returnValue = favoriteMaterials_var.itemById(id) ``` ```` |

"favoriteMaterials\_var" is a variable referencing a [FavoriteMaterials](FavoriteMaterials.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Material](Material.htm) | Returns the specified material or null if there isn't a matching ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the material to return. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |