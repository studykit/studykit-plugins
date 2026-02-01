# UserParameter.deleteMe Method

Parent Object: [UserParameter](UserParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/UserParameter.h>

## Description

Deletes the user parameter A parameter can only be deleted if it is a UserParameter and it is not referenced by other parameters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userParameter\_var" is a variable referencing a [UserParameter](UserParameter.htm) object.```` ``` returnValue = userParameter_var.deleteMe() ``` ```` |

"userParameter\_var" is a variable referencing a [UserParameter](UserParameter.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns a bool indicating if the delete was successful or not. Bug!!! Currently returning true if the parameter can't be deleted because it is being referenced by other parameters. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |