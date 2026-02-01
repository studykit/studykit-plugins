# AsBuiltJoints.itemByName Method

Parent Object: [AsBuiltJoints](AsBuiltJoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/AsBuiltJoints.h>

## Description

Function that returns the specified as-built joint using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object.```` ``` returnValue = asBuiltJoints_var.itemByName(name) ``` ```` |

"asBuiltJoints\_var" is a variable referencing an [AsBuiltJoints](AsBuiltJoints.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [AsBuiltJoint](AsBuiltJoint.htm) | Returns the specified item or null if an invalid name was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the item within the collection to return. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |