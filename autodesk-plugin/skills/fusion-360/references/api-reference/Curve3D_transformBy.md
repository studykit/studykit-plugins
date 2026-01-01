# Curve3D.transformBy Method

Parent Object: [Curve3D](Curve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Curve3D.h>

## Description

Transforms this curve in 3D space.

## Syntax

* [Python](#Python)
* [C++](#C++)

"curve3D\_var" is a variable referencing a [Curve3D](Curve3D.htm) object.```` ``` returnValue = curve3D_var.transformBy(matrix) ``` ```` |

"curve3D\_var" is a variable referencing a [Curve3D](Curve3D.htm) object. |

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

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |