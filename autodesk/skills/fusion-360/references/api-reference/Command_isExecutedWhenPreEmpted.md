# Command.isExecutedWhenPreEmpted Property

Parent Object: [Command](Command.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Specifies what the behavior will be when a command is preempted by the user executing another command. If true (the default), and all of the current inputs are valid, the command will be executed just the same as if the user clicked the OK button. If false, the command is terminated.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a Command object. |

"command\_var" is a variable referencing a Command object. ```` ``` #include <Core/UserInterface/Command.h>  // Get the value of the property. boolean propertyValue = command_var->isExecutedWhenPreEmpted();  // Set the value of the property, where value_var is a boolean. bool returnValue = command_var->isExecutedWhenPreEmpted(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |