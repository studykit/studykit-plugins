# Matrix2D.setToRotation Method

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Sets this matrix to the matrix of rotation by the specified angle, through the specified origin.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object.```` ``` returnValue = matrix2D_var.setToRotation(angle, origin) ``` ```` |

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angle | double | The rotation angle in radians. |
| origin | [Point2D](Point2D.htm) | The origin point of the rotation. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |