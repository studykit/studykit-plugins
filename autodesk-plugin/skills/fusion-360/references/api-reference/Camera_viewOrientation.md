# Camera.viewOrientation Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

Sets the camera to a standard orientation. If this is set, it will result in resetting all the camera values except the camera type. The orientation is based on the current orientation defined by the ViewCube. This means, that the view orientations cannot be expected to be consistent from one view to another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object. |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. ViewOrientations propertyValue = camera_var->viewOrientation();  // Set the value of the property, where value_var is a ViewOrientations. bool returnValue = camera_var->viewOrientation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ViewOrientations](ViewOrientations.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |