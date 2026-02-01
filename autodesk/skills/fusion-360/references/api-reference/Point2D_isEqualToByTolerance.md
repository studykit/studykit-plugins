# Point2D.isEqualToByTolerance Method

Parent Object: [Point2D](Point2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point2D.h>

## Description

Checks to see if this point and another point are equal within the specified tolerance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point2D\_var" is a variable referencing a [Point2D](Point2D.htm) object.```` ``` returnValue = point2D_var.isEqualToByTolerance(point, tolerance) ``` ```` |

"point2D\_var" is a variable referencing a [Point2D](Point2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the points are equal (have identical coordinates). |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point2D](Point2D.htm) | The point to compare for equality. |
| tolerance | double | The tolerance, in centimeters, to use when comparing the two points. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |