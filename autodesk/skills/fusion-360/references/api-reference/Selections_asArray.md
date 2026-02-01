# Selections.asArray Method

Parent Object: [Selections](Selections.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Selections.h>

## Description

Returns an array containing all of the current selections. This is useful in cases where you need to iterate over the set of selected entities but need to create or edit data as you process each one. Selections are fragile and creation and edit operations will clear the selections so you won't have access to the complete list after processing the first one.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selections\_var" is a variable referencing a [Selections](Selections.htm) object.```` ``` returnValue = selections_var.asArray() ``` ```` |

"selections\_var" is a variable referencing a [Selections](Selections.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Selection](Selection.htm)[] | Returns an array of all of the current selections. Selection objects are returned so you'll need to call their entity properties to get the actual selected entity. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |