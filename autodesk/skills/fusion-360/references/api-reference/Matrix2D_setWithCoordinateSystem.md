# Matrix2D.setWithCoordinateSystem Method

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Reset this matrix to align with a specific coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object.```` ``` returnValue = matrix2D_var.setWithCoordinateSystem(origin, xAxis, yAxis) ``` ```` |

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
| origin | [Point2D](Point2D.htm) | The origin point of the coordinate system. |
| xAxis | [Vector2D](Vector2D.htm) | The x axis direction of the coordinate system. |
| yAxis | [Vector2D](Vector2D.htm) | The y axis direction of the coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |