# SetupEvent.add Method

Parent Object: [SetupEvent](SetupEvent.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/SetupEvent.h>

## Description

Add a handler to be notified when the file event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setupEvent\_var" is a variable referencing a [SetupEvent](SetupEvent.htm) object.```` ``` returnValue = setupEvent_var.add(handler) ``` ```` |

"setupEvent\_var" is a variable referencing a [SetupEvent](SetupEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [SetupEventHandler](SetupEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version April 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |