# Point3D.transformBy Method

Parent Object: [Point3D](Point3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Transforms the point using the provided matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"point3D\_var" is a variable referencing a [Point3D](Point3D.htm) object.```` ``` returnValue = point3D_var.transformBy(matrix) ``` ```` |

"point3D\_var" is a variable referencing a [Point3D](Point3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix3D](Matrix3D.htm) | The Matrix3D object that defines the transformation. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |