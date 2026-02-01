# TangentRelationships.itemByName Method

Parent Object: [TangentRelationships](TangentRelationships.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/TangentRelationships.h>

## Description

Function that returns the specified tangent relationship using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object.```` ``` returnValue = tangentRelationships_var.itemByName(name) ``` ```` |

"tangentRelationships\_var" is a variable referencing a [TangentRelationships](TangentRelationships.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [TangentRelationship](TangentRelationship.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the item within the collection to return. |

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |