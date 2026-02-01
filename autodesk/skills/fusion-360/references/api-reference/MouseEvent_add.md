# MouseEvent.add Method

Parent Object: [MouseEvent](MouseEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/MouseEvent.h>

## Description

Adds an event handler to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"mouseEvent\_var" is a variable referencing a [MouseEvent](MouseEvent.htm) object.```` ``` returnValue = mouseEvent_var.add(handler) ``` ```` |

"mouseEvent\_var" is a variable referencing a [MouseEvent](MouseEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [MouseEventHandler](MouseEventHandler.htm) | The client implemented MouseEventHandler to be called when this event is triggered. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |