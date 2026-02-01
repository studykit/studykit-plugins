# CameraEventArgs.viewport Property

Parent Object: [CameraEventArgs](CameraEventArgs.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CameraEventArgs.h>

## Description

Returns the viewport that the modified camera is associated with.

## Syntax

* [Python](#Python)
* [C++](#C++)

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. |

"cameraEventArgs\_var" is a variable referencing a CameraEventArgs object. ```` ``` #include <Core/Application/CameraEventArgs.h>  // Get the value of the property. Ptr<Viewport> propertyValue = cameraEventArgs_var->viewport(); ``` ```` |

## Property Value

This is a read only property whose value is a [Viewport](Viewport.htm).

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |