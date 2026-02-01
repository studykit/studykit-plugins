# SetupChangeEvent.add Method

Parent Object: [SetupChangeEvent](SetupChangeEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupChangeEvent.h>

## Description

Add a handler to be notified when the file event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupChangeEvent\_var" is a variable referencing a [SetupChangeEvent](SetupChangeEvent.htm) object.```` ``` returnValue = setupChangeEvent_var.add(handler) ``` ```` |

"setupChangeEvent\_var" is a variable referencing a [SetupChangeEvent](SetupChangeEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SetupChangeEventHandler](SetupChangeEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |