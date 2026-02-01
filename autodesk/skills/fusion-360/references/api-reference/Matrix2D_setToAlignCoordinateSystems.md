# Matrix2D.setToAlignCoordinateSystems Method

Parent Object: [Matrix2D](Matrix2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix2D.h>

## Description

Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system.

## Syntax

* [Python](#Python)
* [C++](#C++)

"matrix2D\_var" is a variable referencing a [Matrix2D](Matrix2D.htm) object.```` ``` returnValue = matrix2D_var.setToAlignCoordinateSystems(fromOrigin, fromXAxis, fromYAxis, toOrigin, toXAxis, toYAxis) ``` ```` |

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
| fromOrigin | [Point2D](Point2D.htm) | The origin point of the from coordinate system. |
| fromXAxis | [Vector2D](Vector2D.htm) | The x axis direction of the from coordinate system. |
| fromYAxis | [Vector2D](Vector2D.htm) | The y axis direction of the from coordinate system. |
| toOrigin | [Point2D](Point2D.htm) | The origin point of the to coordinate system. |
| toXAxis | [Vector2D](Vector2D.htm) | The x axis direction of the to coordinate system. |
| toYAxis | [Vector2D](Vector2D.htm) | The y axis direction of the to coordinate system. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |