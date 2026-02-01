# CameraEvent.add Method

Parent Object: [CameraEvent](CameraEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEvent.h>

## Description

Add a handler to be notified when the event occurs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEvent\_var" is a variable referencing a [CameraEvent](CameraEvent.htm) object.```` ``` returnValue = cameraEvent_var.add(handler) ``` ```` |

"cameraEvent\_var" is a variable referencing a [CameraEvent](CameraEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the addition of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CameraEventHandler](CameraEventHandler.htm) | The handler object to be called when this event is fired. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |