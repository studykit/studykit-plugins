# JointList.itemByName Method

Parent Object: [JointList](JointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointList.h>

## Description

Function that returns the specified joint using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointList\_var" is a variable referencing a [JointList](JointList.htm) object.```` ``` returnValue = jointList_var.itemByName(name) ``` ```` |

"jointList\_var" is a variable referencing a [JointList](JointList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Joint](Joint.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the item within the list to return. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |