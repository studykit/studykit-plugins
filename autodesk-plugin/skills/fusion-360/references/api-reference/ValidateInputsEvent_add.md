# ValidateInputsEvent.add Method

Parent Object: [ValidateInputsEvent](ValidateInputsEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ValidateInputsEvent.h>

## Description

Adds an event handler to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"validateInputsEvent\_var" is a variable referencing a [ValidateInputsEvent](ValidateInputsEvent.htm) object.```` ``` returnValue = validateInputsEvent_var.add(handler) ``` ```` |

"validateInputsEvent\_var" is a variable referencing a [ValidateInputsEvent](ValidateInputsEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ValidateInputsEventHandler](ValidateInputsEventHandler.htm) | The client implemented ValidateInputsEventHandler to be called when this event is triggered. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |