# UserInterface.terminateActiveCommand Method

Parent Object: [UserInterface](UserInterface.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterface.h>

## Description

Method that causes the currently active (running) command to be terminated

## Remarks

The terminateActiveCommand method is not supported within any of the Command related events because it results in the termination of the current command, which is your running command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object.```` ``` returnValue = userInterface_var.terminateActiveCommand() ``` ```` |

"userInterface\_var" is a variable referencing a [UserInterface](UserInterface.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if terminating the active command was successful. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |