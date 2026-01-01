# JointOrigins.item Method

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

Function that returns the specified joint origin using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object.```` ``` returnValue = jointOrigins_var.item(index) ``` ```` |

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns the specified item or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the item within the collection to return. The first item in the collection has an index of 0. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |