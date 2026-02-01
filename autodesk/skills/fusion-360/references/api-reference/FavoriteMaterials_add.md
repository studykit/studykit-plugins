# FavoriteMaterials.add Method

Parent Object: [FavoriteMaterials](FavoriteMaterials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/FavoriteMaterials.h>

## Description

Adds an existing material to the Favorites list

## Syntax

* [Python](#Python)
* [C++](#C++)

"favoriteMaterials\_var" is a variable referencing a [FavoriteMaterials](FavoriteMaterials.htm) object.```` ``` returnValue = favoriteMaterials_var.add(material) ``` ```` |

"favoriteMaterials\_var" is a variable referencing a [FavoriteMaterials](FavoriteMaterials.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Material](Material.htm) | Returns the Material added to the favorites list or null if the operation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| material | [Material](Material.htm) | The material to be added to the favorites list. This can come from a Library or from a Design. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |