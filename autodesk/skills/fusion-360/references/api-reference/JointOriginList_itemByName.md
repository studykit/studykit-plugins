# JointOriginList.itemByName Method

Parent Object: [JointOriginList](JointOriginList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOriginList.h>

## Description

Function that returns the specified joint origin using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOriginList\_var" is a variable referencing a [JointOriginList](JointOriginList.htm) object.```` ``` returnValue = jointOriginList_var.itemByName(name) ``` ```` |

"jointOriginList\_var" is a variable referencing a [JointOriginList](JointOriginList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns the specified item or null if an invalid name was specified. |

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