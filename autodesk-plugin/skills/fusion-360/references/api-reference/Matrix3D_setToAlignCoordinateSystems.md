# Matrix3D.setToAlignCoordinateSystems Method

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object.```` ``` returnValue = matrix3D_var.setToAlignCoordinateSystems(fromOrigin, fromXAxis, fromYAxis, fromZAxis, toOrigin, toXAxis, toYAxis, toZAxis) ``` ```` |

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| fromOrigin | [Point3D](Point3D.htm) | The origin point of the from coordinate system. |
| fromXAxis | [Vector3D](Vector3D.htm) | The x axis direction of the from coordinate system. |
| fromYAxis | [Vector3D](Vector3D.htm) | The y axis direction of the from coordinate system. |
| fromZAxis | [Vector3D](Vector3D.htm) | The z axis direction of the from coordinate system. |
| toOrigin | [Point3D](Point3D.htm) | The origin point of the to coordinate system. |
| toXAxis | [Vector3D](Vector3D.htm) | The x axis direction of the to coordinate system. |
| toYAxis | [Vector3D](Vector3D.htm) | The y axis direction of the to coordinate system. |
| toZAxis | [Vector3D](Vector3D.htm) | The z axis direction of the to coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |