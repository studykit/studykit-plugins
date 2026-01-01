# Point3D.isEqualToByTolerance Method

Parent Object: [Point3D](Point3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Checks to see if this point and another point are equal within the specified tolerance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point3D\_var" is a variable referencing a [Point3D](Point3D.htm) object.```` ``` returnValue = point3D_var.isEqualToByTolerance(point, tolerance) ``` ```` |

"point3D\_var" is a variable referencing a [Point3D](Point3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the points are equal (have identical coordinates). |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to compare for equality. |
| tolerance | double | The tolerance, in centimeters, to use when comparing the two points. |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |