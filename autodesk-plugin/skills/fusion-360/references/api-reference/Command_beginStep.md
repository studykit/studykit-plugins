# Command.beginStep Method![](../images/TestTubeLarge.png)

Parent Object: [Command](Command.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::core" and the header file is <Core/UserInterface/Command.h>

## Description

Begin a transacted step within the command's transaction. If the all of the command inputs are valid, this will trigger the execute event for the current step.

## Syntax

* [Python](#Python)
* [C++](#C++)

"command\_var" is a variable referencing a [Command](Command.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"command\_var" is a variable referencing a [Command](Command.htm) object.  ```` ``` #include <Core/UserInterface/Command.h>  // Uses no optional arguments. returnValue = command_var->beginStep();  // Uses optional arguments. returnValue = command_var->beginStep(makeExistingStepNonUndoable); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if beginning the step was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| makeExistingStepNonUndoable | boolean | If true the current step will not be undo-able.   This is an optional argument whose default value is False. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |