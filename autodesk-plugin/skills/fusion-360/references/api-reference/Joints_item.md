# Joints.item Method

Parent Object: [Joints](Joints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Joints.h>

## Description

Function that returns the specified joint using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"joints\_var" is a variable referencing a [Joints](Joints.htm) object.```` ``` returnValue = joints_var.item(index) ``` ```` |

"joints\_var" is a variable referencing a [Joints](Joints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Joint](Joint.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version July 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |