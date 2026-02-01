# ApplicationCommandEvent.remove Method

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

Removes a handler from this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an [ApplicationCommandEvent](ApplicationCommandEvent.htm) object.```` ``` returnValue = applicationCommandEvent_var.remove(handler) ``` ```` |

"applicationCommandEvent\_var" is a variable referencing an [ApplicationCommandEvent](ApplicationCommandEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was found and removed from the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ApplicationCommandEventHandler](ApplicationCommandEventHandler.htm) | An ApplicationCommandEventHandler that was previously added to this event with the add method. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |