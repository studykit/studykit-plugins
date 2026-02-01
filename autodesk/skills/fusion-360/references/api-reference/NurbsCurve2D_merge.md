# NurbsCurve2D.merge Method

Parent Object: [NurbsCurve2D](NurbsCurve2D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/NurbsCurve2D.h>

## Description

Define a new NURBS curve that is the result of combining this NURBS curve with another NURBS curve. The curves are merged with the end point of the current curve merging with the start point of the other curve. The curves are forced to join even if they are not physically touching so you will typically want to make sure the end and start points of the curves are where you expect them to be.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nurbsCurve2D\_var" is a variable referencing a [NurbsCurve2D](NurbsCurve2D.htm) object.```` ``` returnValue = nurbsCurve2D_var.merge(nurbsCurve) ``` ```` |

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
| nurbsCurve | [NurbsCurve2D](NurbsCurve2D.htm) | The NURBS curve to combine with |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |