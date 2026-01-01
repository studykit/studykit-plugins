# Command.doExecutePreview Method

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Causes the executePreview event of this command to be fired. This is most useful when there is no command dialog (no command inputs where created) and the isAutoExecute property has been set to False. This allows you to force the preview to be generated instead of relying on changing command inputs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` returnValue = command_var.doExecutePreview() ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the execute Preview event was successfully fired.. |

## Version

Introduced in version April 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |