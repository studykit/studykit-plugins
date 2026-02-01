# Point2D.isEqualTo Method

Parent Object: [Point2D](Point2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point2D.h>

## Description

Checks to see if this point and another point are equal (have identical coordinates). The comparison is done within the modeling tolerance which can be found with the Application.pointTolerance property. If you want to compare two points with any other tolerance you can use the isEqualToByTolerance method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point2D\_var" is a variable referencing a [Point2D](Point2D.htm) object.```` ``` returnValue = point2D_var.isEqualTo(point) ``` ```` |

"point2D\_var" is a variable referencing a [Point2D](Point2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the points are equal. (have identical coordinates) |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point2D](Point2D.htm) | The point to compare for equality |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |