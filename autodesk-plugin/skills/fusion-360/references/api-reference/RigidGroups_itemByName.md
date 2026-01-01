# RigidGroups.itemByName Method

Parent Object: [RigidGroups](RigidGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroups.h>

## Description

Function that returns the specified rigid group using a name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroups\_var" is a variable referencing a [RigidGroups](RigidGroups.htm) object.```` ``` returnValue = rigidGroups_var.itemByName(name) ``` ```` |

"rigidGroups\_var" is a variable referencing a [RigidGroups](RigidGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RigidGroup](RigidGroup.htm) | Returns the specified item or null if an invalid name was specified. |

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