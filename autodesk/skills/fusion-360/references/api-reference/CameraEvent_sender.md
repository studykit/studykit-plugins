# CameraEvent.sender Property

Parent Object: [CameraEvent](CameraEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEvent.h>

## Description

The object that is firing the event. For example, in the case of a command input event this will return the command.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEvent\_var" is a variable referencing a CameraEvent object. |

"cameraEvent\_var" is a variable referencing a CameraEvent object. ```` ``` #include <Core/Application/CameraEvent.h>  // Get the value of the property. Ptr<Base> propertyValue = cameraEvent_var->sender(); ``` ```` |

## Property Value

This is a read only property whose value is a [Base](Base.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |