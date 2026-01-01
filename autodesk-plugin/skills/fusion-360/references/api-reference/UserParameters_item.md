# UserParameters.item Method

Parent Object: [UserParameters](UserParameters.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameters.h>

## Description

Function that returns the specified User Parameter using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object.```` ``` returnValue = userParameters_var.item(index) ``` ```` |

"userParameters\_var" is a variable referencing a [UserParameters](UserParameters.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [UserParameter](UserParameter.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |