# NurbsCurve3D.merge Method

Parent Object: [NurbsCurve3D](NurbsCurve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Define a new NURBS curve that is the result of combining this NURBS curve with another NURBS curve.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve3D\_var" is a variable referencing a [NurbsCurve3D](NurbsCurve3D.htm) object.```` ``` returnValue = nurbsCurve3D_var.merge(nurbsCurve) ``` ```` |

"nurbsCurve3D\_var" is a variable referencing a [NurbsCurve3D](NurbsCurve3D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NurbsCurve3D](NurbsCurve3D.htm) | Returns a new NurbsCurve3D object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| nurbsCurve | [NurbsCurve3D](NurbsCurve3D.htm) | The NURBS curve to combine with. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |