# Camera.perspectiveAngle Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

Gets and sets the perspective angle of the camera. This property is only valid when the CameraType property is either Perspective or PerspectiveWithOrthoFaces.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object. |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. double propertyValue = camera_var->perspectiveAngle();  // Set the value of the property, where value_var is a double. bool returnValue = camera_var->perspectiveAngle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |