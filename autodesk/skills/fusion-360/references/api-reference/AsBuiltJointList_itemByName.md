# AsBuiltJointList.itemByName Method

Parent Object: [AsBuiltJointList](AsBuiltJointList.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJointList.h>

## Description

Function that returns the specified as-built joint using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJointList\_var" is a variable referencing an [AsBuiltJointList](AsBuiltJointList.htm) object.```` ``` returnValue = asBuiltJointList_var.itemByName(name) ``` ```` |

"asBuiltJointList\_var" is a variable referencing an [AsBuiltJointList](AsBuiltJointList.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the specified item or null if an invalid name was specified. |

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