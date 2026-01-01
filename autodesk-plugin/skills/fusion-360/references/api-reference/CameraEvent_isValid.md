# CameraEvent.isValid Property

Parent Object: [CameraEvent](CameraEvent.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEvent.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEvent\_var" is a variable referencing a CameraEvent object. |

"cameraEvent\_var" is a variable referencing a CameraEvent object. ```` ``` #include <Core/Application/CameraEvent.h>  // Get the value of the property. boolean propertyValue = cameraEvent_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |