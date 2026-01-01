# JointOriginList.item Method

Parent Object: [JointOriginList](JointOriginList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginList.h>

## Description

Function that returns the specified joint origin using an index into the list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginList\_var" is a variable referencing a [JointOriginList](JointOriginList.htm) object.```` ``` returnValue = jointOriginList_var.item(index) ``` ```` |

"jointOriginList\_var" is a variable referencing a [JointOriginList](JointOriginList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the list to return. The first item in the list has an index of 0. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |