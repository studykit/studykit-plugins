# CameraEvent.remove Method

Parent Object: [CameraEvent](CameraEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEvent.h>

## Description

Removes a handler from the event.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEvent\_var" is a variable referencing a [CameraEvent](CameraEvent.htm) object.```` ``` returnValue = cameraEvent_var.remove(handler) ``` ```` |

"cameraEvent\_var" is a variable referencing a [CameraEvent](CameraEvent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if removal of the handler was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| handler | [CameraEventHandler](CameraEventHandler.htm) | The handler object to be removed from the event. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |