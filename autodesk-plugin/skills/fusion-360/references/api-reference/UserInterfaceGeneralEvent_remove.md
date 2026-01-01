# UserInterfaceGeneralEvent.remove Method

Parent Object: [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEvent\_var" is a variable referencing a [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm) object.```` ``` returnValue = userInterfaceGeneralEvent_var.remove(handler) ``` ```` |

"userInterfaceGeneralEvent\_var" is a variable referencing a [UserInterfaceGeneralEvent](UserInterfaceGeneralEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [UserInterfaceGeneralEventHandler](UserInterfaceGeneralEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |