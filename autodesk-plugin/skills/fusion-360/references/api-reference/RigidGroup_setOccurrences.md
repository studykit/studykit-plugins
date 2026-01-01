# RigidGroup.setOccurrences Method

Parent Object: [RigidGroup](RigidGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/RigidGroup.h>

## Description

Sets which occurrences are to be part of this rigid group.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rigidGroup\_var" is a variable referencing a [RigidGroup](RigidGroup.htm) object.```` ``` returnValue = rigidGroup_var.setOccurrences(occurrences, includeChildren) ``` ```` |

"rigidGroup\_var" is a variable referencing a [RigidGroup](RigidGroup.htm) object.  ```` ``` #include <Fusion/Components/RigidGroup.h>  returnValue = rigidGroup_var->setOccurrences(occurrences, includeChildren); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrences | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the occurrences to use in creating the rigid group. |
| includeChildren | boolean | Boolean indicating if the children of the input occurrences should be included in the rigid group. |

## Version

Introduced in version September 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |