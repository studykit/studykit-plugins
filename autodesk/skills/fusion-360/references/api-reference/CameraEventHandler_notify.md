# CameraEventHandler.notify Method

Parent Object: [CameraEventHandler](CameraEventHandler.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEventHandler.h>

## Description

The function called by Fusion when the associated event is fired.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEventHandler\_var" is a variable referencing a [CameraEventHandler](CameraEventHandler.htm) object.```` ``` returnValue = cameraEventHandler_var.notify(eventArgs) ``` ```` |

"cameraEventHandler\_var" is a variable referencing a [CameraEventHandler](CameraEventHandler.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| eventArgs | [CameraEventArgs](CameraEventArgs.htm) | Returns an object that provides access to additional information associated with the event. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |