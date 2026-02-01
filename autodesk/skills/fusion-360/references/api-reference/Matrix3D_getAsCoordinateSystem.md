# Matrix3D.getAsCoordinateSystem Method

Parent Object: [Matrix3D](Matrix3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Gets the matrix data as the components that define a coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix3D\_var" is a variable referencing a [Matrix3D](Matrix3D.htm) object. |

```` ```  #include <Core/Geometry/Matrix3D.h ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point3D](Point3D.htm) | The output origin point of the coordinate system. |
| xAxis | [Vector3D](Vector3D.htm) | The output x axis direction of the coordinate system. |
| yAxis | [Vector3D](Vector3D.htm) | The output y axis direction of the coordinate system. |
| zAxis | [Vector3D](Vector3D.htm) | The output z axis direction of the coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |