# Materials.item Method

Parent Object: [Materials](Materials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

Returns the specified Material using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materials\_var" is a variable referencing a [Materials](Materials.htm) object.```` ``` returnValue = materials_var.item(index) ``` ```` |

"materials\_var" is a variable referencing a [Materials](Materials.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Material](Material.htm) | Returns the specified material or null if an invalid index is specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the material to return where the first item in the collection is 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |