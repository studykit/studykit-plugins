# AsBuiltJoints.item Method

Parent Object: [AsBuiltJoints](AsBuiltJoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoints.h>

## Description

Function that returns the specified as-built joint using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object.```` ``` returnValue = asBuiltJoints_var.item(index) ``` ```` |

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the specified item or null if an invalid index was specified. |

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