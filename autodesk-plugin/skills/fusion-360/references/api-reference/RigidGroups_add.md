# RigidGroups.add Method

Parent Object: [RigidGroups](RigidGroups.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroups.h>

## Description

Creates a new rigid group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroups\_var" is a variable referencing a [RigidGroups](RigidGroups.htm) object.```` ``` returnValue = rigidGroups_var.add(occurrences, includeChildren) ``` ```` |

"rigidGroups\_var" is a variable referencing a [RigidGroups](RigidGroups.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RigidGroup](RigidGroup.htm) | Returns the new RigidGroup object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrences | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the occurrences to use in creating the rigid group. |
| includeChildren | boolean | Boolean indicating if the children of the input occurrences should be included in the rigid group. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Rigid Group API Sample](RigidGroupSample_Sample.htm) | Demonstrates creating a new Rigid Group. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |