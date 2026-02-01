# BRepBody.pointContainment Method

Parent Object: [BRepBody](BRepBody.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepBody.h>

## Description

Determines the relationship of the input point with respect to this body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object.```` ``` returnValue = bRepBody_var.pointContainment(point) ``` ```` |

"bRepBody\_var" is a variable referencing a [BRepBody](BRepBody.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [PointContainment](PointContainment.htm) | Returns a value from the PointContainment enum indicating the relationship of the input point to the body. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Point3D](Point3D.htm) | The point to do the containment check for. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |