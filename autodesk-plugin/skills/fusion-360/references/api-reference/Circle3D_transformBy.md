# Circle3D.transformBy Method

Parent Object: [Circle3D](Circle3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Circle3D.h>

## Description

Transforms this curve in 3D space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"circle3D\_var" is a variable referencing a [Circle3D](Circle3D.htm) object.```` ``` returnValue = circle3D_var.transformBy(matrix) ``` ```` |

"circle3D\_var" is a variable referencing a [Circle3D](Circle3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Return true if the transform was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix3D](Matrix3D.htm) | A 3D matrix that defines the transform to apply to the curve. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |