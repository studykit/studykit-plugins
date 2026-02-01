# UserInterfaceGeneralEventHandler.notify Method

Parent Object: [UserInterfaceGeneralEventHandler](UserInterfaceGeneralEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/UserInterfaceGeneralEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"userInterfaceGeneralEventHandler\_var" is a variable referencing a [UserInterfaceGeneralEventHandler](UserInterfaceGeneralEventHandler.htm) object.```` ``` returnValue = userInterfaceGeneralEventHandler_var.notify(eventArgs) ``` ```` |

"userInterfaceGeneralEventHandler\_var" is a variable referencing a [UserInterfaceGeneralEventHandler](UserInterfaceGeneralEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [UserInterfaceGeneralEventArgs](UserInterfaceGeneralEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version March 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |