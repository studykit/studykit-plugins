# SelectionCommandInput.setSelectionLimits Method

Parent Object: [SelectionCommandInput](SelectionCommandInput.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/SelectionCommandInput.h>

## Description

Defines the limits for the number of selections associated with this input. A maximum value of 0 indicates that there is no maximum.

## Syntax

* [Python](#Python)
* [C++](#C++)

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"selectionCommandInput\_var" is a variable referencing a [SelectionCommandInput](SelectionCommandInput.htm) object.  ```` ``` #include <Core/UserInterface/SelectionCommandInput.h>  // Uses no optional arguments. returnValue = selectionCommandInput_var->setSelectionLimits(minimum);  // Uses optional arguments. returnValue = selectionCommandInput_var->setSelectionLimits(minimum, maximum); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the limits were successfully set. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| minimum | uinteger | The minimum number of selections required. A value of zero means that there is no minimum limit. |
| maximum | uinteger | The maximum number of selections required. A value of zero means that there is no maximum limit. If maximum is equal to minimum, then exactly that number of selections is required.   This is an optional argument whose default value is 0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Command Inputs API Sample](CommandInputsSample_Sample.htm) | Creates a command dialog that demonstrates all of the available command inputs.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/CommandInputsResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |