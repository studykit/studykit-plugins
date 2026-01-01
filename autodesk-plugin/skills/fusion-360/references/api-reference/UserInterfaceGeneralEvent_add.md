# UserInterfaceGeneralEvent.add Method

Parent Object: [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEvent\_var" is a variable referencing a [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm) object.```` ``` returnValue = userInterfaceGeneralEvent_var.add(handler) ``` ```` |

"userInterfaceGeneralEvent\_var" is a variable referencing a [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [UserInterfaceGeneralEventHandler](UserInterfaceGeneralEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |