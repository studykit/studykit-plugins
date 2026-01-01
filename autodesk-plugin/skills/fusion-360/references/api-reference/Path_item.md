# Path.item Method

Parent Object: [Path](Path.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

Function that returns the specified PathEntity using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"path\_var" is a variable referencing a [Path](Path.htm) object.```` ``` returnValue = path_var.item(index) ``` ```` |

"path\_var" is a variable referencing a [Path](Path.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PathEntity](PathEntity.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |