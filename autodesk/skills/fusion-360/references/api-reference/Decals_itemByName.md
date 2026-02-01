# Decals.itemByName Method

Parent Object: [Decals](Decals.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decals.h>

## Description

Returns the specified decal using the name of the decal.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decals\_var" is a variable referencing a [Decals](Decals.htm) object.```` ``` returnValue = decals_var.itemByName(name) ``` ```` |

"decals\_var" is a variable referencing a [Decals](Decals.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Decal](Decal.htm) | Returns the specified Decal object, if it exists. Otherwise it returns null. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the decal as seen in the browser and timeline. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |