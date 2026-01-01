# Matrix2D.getAsCoordinateSystem Method

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Gets the matrix data as the components that define a coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object. |

```` ```  #include <Core/Geometry/Matrix2D.h ``` ```` |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| origin | [Point2D](Point2D.htm) | The output origin point of the coordinate system. |
| xAxis | [Vector2D](Vector2D.htm) | The output x axis direction of the coordinate system. |
| yAxis | [Vector2D](Vector2D.htm) | The output y axis direction of the coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |