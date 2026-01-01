# Decals.item Method

Parent Object: [Decals](Decals.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Decals.h>

## Description

Returns the specified Decal object using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"decals\_var" is a variable referencing a [Decals](Decals.htm) object.```` ``` returnValue = decals_var.item(index) ``` ```` |

"decals\_var" is a variable referencing a [Decals](Decals.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Decal](Decal.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |