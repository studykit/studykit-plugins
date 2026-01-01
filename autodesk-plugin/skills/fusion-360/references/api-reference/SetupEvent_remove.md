# SetupEvent.remove Method

Parent Object: [SetupEvent](SetupEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEvent\_var" is a variable referencing a [SetupEvent](SetupEvent.htm) object.```` ``` returnValue = setupEvent_var.remove(handler) ``` ```` |

"setupEvent\_var" is a variable referencing a [SetupEvent](SetupEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SetupEventHandler](SetupEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |