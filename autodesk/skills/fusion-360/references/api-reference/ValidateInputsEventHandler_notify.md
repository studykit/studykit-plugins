# ValidateInputsEventHandler.notify Method

Parent Object: [ValidateInputsEventHandler](ValidateInputsEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEventHandler.h>

## Description

This notify member is called when an event is triggered from any event that this handler has been added to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEventHandler\_var" is a variable referencing a [ValidateInputsEventHandler](ValidateInputsEventHandler.htm) object.```` ``` returnValue = validateInputsEventHandler_var.notify(eventArgs) ``` ```` |

"validateInputsEventHandler\_var" is a variable referencing a [ValidateInputsEventHandler](ValidateInputsEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [ValidateInputsEventArgs](ValidateInputsEventArgs.htm) | The arguments object with details about this event and the firing ValidateInputsEvent. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |