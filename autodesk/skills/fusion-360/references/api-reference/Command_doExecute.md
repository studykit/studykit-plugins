# Command.doExecute Method

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Causes the execution of this command which results in the execute event being fired. This is the same effect as the user clicking the "OK" button in the command dialog and is most useful when there is no command dialog (no command inputs where created) and the isAutoExecute property has been set to False. This allows you to execute the command through code.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` returnValue = command_var.doExecute(terminate) ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the execution of the command was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| terminate | boolean | In the case where there isn't a command dialog you can also use the terminate argument to specify if the command should terminate after execution or continue running. This is similar to the sketch line command where each line placement results in the creation of an undo-able line but the command continues to run to allow additional lines to be placed. |

## Version

Introduced in version April 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |