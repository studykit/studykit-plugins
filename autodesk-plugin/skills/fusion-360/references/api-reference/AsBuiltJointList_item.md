# AsBuiltJointList.item Method

Parent Object: [AsBuiltJointList](AsBuiltJointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointList.h>

## Description

Function that returns the specified as-built joint using an index into the list.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointList\_var" is a variable referencing an [AsBuiltJointList](AsBuiltJointList.htm) object.```` ``` returnValue = asBuiltJointList_var.item(index) ``` ```` |

"asBuiltJointList\_var" is a variable referencing an [AsBuiltJointList](AsBuiltJointList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the specified item or null if an invalid index was specified. |

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