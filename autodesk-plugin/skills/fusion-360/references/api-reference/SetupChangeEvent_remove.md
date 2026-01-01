# SetupChangeEvent.remove Method

Parent Object: [SetupChangeEvent](SetupChangeEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEvent\_var" is a variable referencing a [SetupChangeEvent](SetupChangeEvent.htm) object.```` ``` returnValue = setupChangeEvent_var.remove(handler) ``` ```` |

"setupChangeEvent\_var" is a variable referencing a [SetupChangeEvent](SetupChangeEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SetupChangeEventHandler](SetupChangeEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |