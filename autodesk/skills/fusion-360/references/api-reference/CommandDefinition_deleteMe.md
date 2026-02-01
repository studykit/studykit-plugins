# CommandDefinition.deleteMe Method

Parent Object: [CommandDefinition](CommandDefinition.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandDefinition.h>

## Description

Deletes this command definition. This is only valid for API created command definitions and will fail if the isNative property is true.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandDefinition\_var" is a variable referencing a [CommandDefinition](CommandDefinition.htm) object.```` ``` returnValue = commandDefinition_var.deleteMe() ``` ```` |

"commandDefinition\_var" is a variable referencing a [CommandDefinition](CommandDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true or false indicating if the deletion was successful. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |