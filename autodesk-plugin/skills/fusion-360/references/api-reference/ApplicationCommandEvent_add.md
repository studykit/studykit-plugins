# ApplicationCommandEvent.add Method

Parent Object: [ApplicationCommandEvent](ApplicationCommandEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/ApplicationCommandEvent.h>

## Description

Adds an event handler object to this event endpoint.

## Syntax

* [Python](#Python)
* [C++](#C++)

"applicationCommandEvent\_var" is a variable referencing an [ApplicationCommandEvent](ApplicationCommandEvent.htm) object.```` ``` returnValue = applicationCommandEvent_var.add(handler) ``` ```` |

"applicationCommandEvent\_var" is a variable referencing an [ApplicationCommandEvent](ApplicationCommandEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the handler was successfully added to the set of event handlers. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [ApplicationCommandEventHandler](ApplicationCommandEventHandler.htm) | The ApplicationCommandEventHandler to be called when this event is triggered. |

## Version

Introduced in version November 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |