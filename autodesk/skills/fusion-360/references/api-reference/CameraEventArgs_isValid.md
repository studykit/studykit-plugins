# CameraEventArgs.isValid Property

Parent Object: [CameraEventArgs](CameraEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEventArgs.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. |

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. ```` ``` #include <Core/Application/CameraEventArgs.h>  // Get the value of the property. boolean propertyValue = cameraEventArgs_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |