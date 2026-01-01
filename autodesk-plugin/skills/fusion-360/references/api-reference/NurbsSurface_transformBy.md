# NurbsSurface.transformBy Method

Parent Object: [NurbsSurface](NurbsSurface.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsSurface.h>

## Description

Updates this surface by transforming it with a given input matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsSurface\_var" is a variable referencing a [NurbsSurface](NurbsSurface.htm) object.```` ``` returnValue = nurbsSurface_var.transformBy(matrix) ``` ```` |

"nurbsSurface\_var" is a variable referencing a [NurbsSurface](NurbsSurface.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the transform was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| matrix | [Matrix3D](Matrix3D.htm) | A 3D matrix that defines the transform to apply to the surface. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |