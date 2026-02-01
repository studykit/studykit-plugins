# Selections.removeByEntity Method

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Removes the selections that are associated with the specified entity from the set of selected entities.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a [Selections](Selections.htm) object.```` ``` returnValue = selections_var.removeByEntity(entity) ``` ```` |

"selections\_var" is a variable referencing a [Selections](Selections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the item was removed or not currently selected. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The entity to remove selections of. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |