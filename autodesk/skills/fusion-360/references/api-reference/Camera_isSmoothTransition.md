# Camera.isSmoothTransition Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

This property controls if Fusion will perform a smooth transition animation from the current camera position to the new position. If this property is set to true, it will smoothly transition. If false, the camera will jump to the position defined by the camera without any animated transition.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object.  ```` ``` # Get the value of the property. propertyValue = camera_var.isSmoothTransition  # Set the value of the property. camera_var.isSmoothTransition = propertyValue ``` ```` |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. boolean propertyValue = camera_var->isSmoothTransition();  // Set the value of the property, where value_var is a boolean. bool returnValue = camera_var->isSmoothTransition(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |