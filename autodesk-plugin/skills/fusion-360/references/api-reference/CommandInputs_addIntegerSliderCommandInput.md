# CommandInputs.addIntegerSliderCommandInput Method

Parent Object: [CommandInputs](CommandInputs.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/CommandInputs.h>

## Description

Adds a new slider input to the command. The value type is integer.

## Syntax

* [Python](#Python)
* [C++](#C++)

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"commandInputs\_var" is a variable referencing a [CommandInputs](CommandInputs.htm) object.  ```` ``` #include <Core/UserInterface/CommandInputs.h>  // Uses no optional arguments. returnValue = commandInputs_var->addIntegerSliderCommandInput(id, name, min, max);  // Uses optional arguments. returnValue = commandInputs_var->addIntegerSliderCommandInput(id, name, min, max, hasTwoSliders); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [IntegerSliderCommandInput](IntegerSliderCommandInput.htm) | Returns the created IntegerSliderCommandInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The unique ID of this command input. It must be unique with respect to the other inputs associated with this command. |
| name | string | The displayed name of this command as seen in the dialog. |
| min | integer | Provides the minimum value. |
| max | integer | Provides the maximum value. |
| hasTwoSliders | boolean | Optional input. Indicates if the slider input has two sliders.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |