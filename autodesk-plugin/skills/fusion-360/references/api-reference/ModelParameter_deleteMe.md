# ModelParameter.deleteMe Method

Parent Object: [ModelParameter](ModelParameter.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/ModelParameter.h>

## Description

Deletes this ModelParameter. As a general rule, model parameters cannot be deleted because features depend on them. However, there are uncommon workflows where a parameter no longer has any dependents and is not automatically deleted. You can use the isDeletable property to see if the parameter is in this state and can successfully be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"modelParameter\_var" is a variable referencing a [ModelParameter](ModelParameter.htm) object.```` ``` returnValue = modelParameter_var.deleteMe() ``` ```` |

"modelParameter\_var" is a variable referencing a [ModelParameter](ModelParameter.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |