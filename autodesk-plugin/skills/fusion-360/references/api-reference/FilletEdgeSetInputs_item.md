# FilletEdgeSetInputs.item Method

Parent Object: [FilletEdgeSetInputs](FilletEdgeSetInputs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/FilletEdgeSetInputs.h>

## Description

Function that returns the specified fillet edge set input using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"filletEdgeSetInputs\_var" is a variable referencing a [FilletEdgeSetInputs](FilletEdgeSetInputs.htm) object.```` ``` returnValue = filletEdgeSetInputs_var.item(index) ``` ```` |

"filletEdgeSetInputs\_var" is a variable referencing a [FilletEdgeSetInputs](FilletEdgeSetInputs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [FilletEdgeSetInput](FilletEdgeSetInput.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. The edge sets are returned in the same order they were created in. |

## Version

Introduced in version November 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |