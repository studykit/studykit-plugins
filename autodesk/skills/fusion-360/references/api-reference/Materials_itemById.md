# Materials.itemById Method

Parent Object: [Materials](Materials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

Returns the Material by it's internal unique ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materials\_var" is a variable referencing a [Materials](Materials.htm) object.```` ``` returnValue = materials_var.itemById(id) ``` ```` |

"materials\_var" is a variable referencing a [Materials](Materials.htm) object. |

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