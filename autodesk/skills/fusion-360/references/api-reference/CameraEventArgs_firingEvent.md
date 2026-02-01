# CameraEventArgs.firingEvent Property

Parent Object: [CameraEventArgs](CameraEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEventArgs.h>

## Description

The event that the firing is in response to.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. |

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. ```` ``` #include <Core/Application/CameraEventArgs.h>  // Get the value of the property. Ptr<Event> propertyValue = cameraEventArgs_var->firingEvent(); ``` ```` |

## Property Value

This is a read only property whose value is an [Event](Event.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |