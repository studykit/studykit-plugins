# NurbsCurve2D.extract Method

Parent Object: [NurbsCurve2D](NurbsCurve2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

Defines a new NURBS curve that is the subset of this NURBS curve in the parameter range of [startParam, endParam]

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve2D\_var" is a variable referencing a [NurbsCurve2D](NurbsCurve2D.htm) object.```` ``` returnValue = nurbsCurve2D_var.extract(startParam, endParam) ``` ```` |

"nurbsCurve2D\_var" is a variable referencing a [NurbsCurve2D](NurbsCurve2D.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [NurbsCurve2D](NurbsCurve2D.htm) | Returns a new NurbsCurve2D object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| startParam | double | The parameter position of the start of the subset. |
| endParam | double | The parameter position of the end of the subset. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |