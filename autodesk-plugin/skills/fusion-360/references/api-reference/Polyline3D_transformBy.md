# Polyline3D.transformBy Method

Parent Object: [Polyline3D](Polyline3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Polyline3D.h>

## Description

Transforms this curve in 3D space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"polyline3D\_var" is a variable referencing a [Polyline3D](Polyline3D.htm) object.```` ``` returnValue = polyline3D_var.transformBy(matrix) ``` ```` |

"polyline3D\_var" is a variable referencing a [Polyline3D](Polyline3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Return true if the transform was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix3D](Matrix3D.htm) | A 3D matrix that defines the transform to apply to the curve. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |