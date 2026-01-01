# Materials.itemByName Method

Parent Object: [Materials](Materials.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/Materials.h>

## Description

Returns the specified Material using the name as seen in the user interface. This often isn't a reliable way of accessing a specific material because materials are not required to be unique.

## Syntax

* [Python](#Python)
* [C++](#C++)

"materials\_var" is a variable referencing a [Materials](Materials.htm) object.```` ``` returnValue = materials_var.itemByName(name) ``` ```` |

"materials\_var" is a variable referencing a [Materials](Materials.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Material](Material.htm) | Returns the specified material or null if there isn't a matching name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the material to return,. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |