# ValidateInputsEvent.remove Method

Parent Object: [ValidateInputsEvent](ValidateInputsEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEvent\_var" is a variable referencing a [ValidateInputsEvent](ValidateInputsEvent.htm) object.```` ``` returnValue = validateInputsEvent_var.remove(handler) ``` ```` |

"validateInputsEvent\_var" is a variable referencing a [ValidateInputsEvent](ValidateInputsEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ValidateInputsEventHandler](ValidateInputsEventHandler.htm) | A ValidateInputsEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |