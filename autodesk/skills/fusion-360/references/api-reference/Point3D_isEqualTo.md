# Point3D.isEqualTo Method

Parent Object: [Point3D](Point3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Checks to see if this point and another point are equal (have identical coordinates). The comparison is done within the modeling tolerance which can be found with the Application.pointTolerance property. If you want to compare two points with any other tolerance you can use the isEqualToByTolerance method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point3D\_var" is a variable referencing a [Point3D](Point3D.htm) object.```` ``` returnValue = point3D_var.isEqualTo(point) ``` ```` |

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

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |