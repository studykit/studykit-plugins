# Camera.cameraType Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

Gets and sets the current camera type.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object. |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. CameraTypes propertyValue = camera_var->cameraType();  // Set the value of the property, where value_var is a CameraTypes. bool returnValue = camera_var->cameraType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CameraTypes](CameraTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |