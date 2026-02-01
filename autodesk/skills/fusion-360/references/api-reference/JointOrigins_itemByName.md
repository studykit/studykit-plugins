# JointOrigins.itemByName Method

Parent Object: [JointOrigins](JointOrigins.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/JointOrigins.h>

## Description

Function that returns the specified joint origin using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object.```` ``` returnValue = jointOrigins_var.itemByName(name) ``` ```` |

"jointOrigins\_var" is a variable referencing a [JointOrigins](JointOrigins.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [JointOrigin](JointOrigin.htm) | Returns the specified item or null if an invalid name was specified. |

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