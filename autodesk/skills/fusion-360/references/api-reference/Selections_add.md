# Selections.add Method

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Adds the entity to the set of currently selected entities. The user will see the entity become selected in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a [Selections](Selections.htm) object.```` ``` returnValue = selections_var.add(entity) ``` ```` |

"selections\_var" is a variable referencing a [Selections](Selections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The entity to select and add to this selection set. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |