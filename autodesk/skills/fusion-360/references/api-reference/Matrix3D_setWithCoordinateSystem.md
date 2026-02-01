# Matrix3D.setWithCoordinateSystem Method

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Sets the matrix based on the components of a coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object.```` ``` returnValue = matrix3D_var.setWithCoordinateSystem(origin, xAxis, yAxis, zAxis) ``` ```` |

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
| origin | [Point3D](Point3D.htm) | The origin point of the coordinate system. |
| xAxis | [Vector3D](Vector3D.htm) | The x axis direction of the coordinate system. |
| yAxis | [Vector3D](Vector3D.htm) | The y axis direction of the coordinate system. |
| zAxis | [Vector3D](Vector3D.htm) | The z axis direction of the coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |