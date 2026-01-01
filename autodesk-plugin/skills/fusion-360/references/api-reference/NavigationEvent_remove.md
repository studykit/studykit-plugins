# NavigationEvent.remove Method

Parent Object: [NavigationEvent](NavigationEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/UserInterface/NavigationEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"navigationEvent\_var" is a variable referencing a [NavigationEvent](NavigationEvent.htm) object.```` ``` returnValue = navigationEvent_var.remove(handler) ``` ```` |

"navigationEvent\_var" is a variable referencing a [NavigationEvent](NavigationEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [NavigationEventHandler](NavigationEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version March 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |