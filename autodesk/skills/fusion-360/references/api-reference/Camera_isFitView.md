# Camera.isFitView Property

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

If this property is true, when this camera is applied to a viewport it will modify the camera such that the entire model is displayed in the viewport. When getting a camera from a viewport or creating a camera using Camera.create(), this property defaults to false.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a Camera object. |

"camera\_var" is a variable referencing a Camera object. ```` ``` #include <Core/Application/Camera.h>  // Get the value of the property. boolean propertyValue = camera_var->isFitView();  // Set the value of the property, where value_var is a boolean. bool returnValue = camera_var->isFitView(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [As-Built Joint Sample](AsBuiltJointSample_Sample.htm) | Demonstrates creating a new As-Built Joint. |
| [Joint Origin Sample](JointOriginSample_Sample.htm) | Demonstrates creating a new Joint Origin. |
| [Rigid Group API Sample](RigidGroupSample_Sample.htm) | Demonstrates creating a new Rigid Group. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |