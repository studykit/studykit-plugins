# TangentRelationships.item Method

Parent Object: [TangentRelationships](TangentRelationships.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationships.h>

## Description

Function that returns the specified tangent relationship using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object.```` ``` returnValue = tangentRelationships_var.item(index) ``` ```` |

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TangentRelationship](TangentRelationship.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |