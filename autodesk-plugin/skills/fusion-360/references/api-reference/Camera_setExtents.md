# Camera.setExtents Method

Parent Object: [Camera](Camera.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Camera.h>

## Description

Sets the extents of the camera. This is only used for orthographic cameras. The extents of a perspective camera is defined by a combination of the position of the eye point (how close the eye is to the model) and the perspective angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"camera\_var" is a variable referencing a [Camera](Camera.htm) object.```` ``` returnValue = camera_var.setExtents(width, height) ``` ```` |

"camera\_var" is a variable referencing a [Camera](Camera.htm) object.  ```` ``` #include <Core/Application/Camera.h>  returnValue = camera_var->setExtents(width, height); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. This will fail in the case it is used for a perspective camera. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| width | double | The width of the extent in centimeters. |
| height | double | The height of the extent in centimeters. |

## Version

Introduced in version October 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |