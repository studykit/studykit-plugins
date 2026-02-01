# NurbsCurve3D.extract Method

Parent Object: [NurbsCurve3D](NurbsCurve3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve3D.h>

## Description

Defines a new NURBS curve that is the subset of this NURBS curve in the parameter range of [startParam, endParam]

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve3D\_var" is a variable referencing a [NurbsCurve3D](NurbsCurve3D.htm) object.```` ``` returnValue = nurbsCurve3D_var.extract(startParam, endParam) ``` ```` |

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
| startParam | double | The parameter position that defines the start of the subset. |
| endParam | double | The parameter position that defines the end of the subset. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |