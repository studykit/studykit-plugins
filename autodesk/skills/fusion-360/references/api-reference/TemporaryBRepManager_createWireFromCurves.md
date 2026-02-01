# TemporaryBRepManager.createWireFromCurves Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Give an array of curve geometry objects, this method creates a new wire body.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object. |

```` ```  #include <Fusion/BRep/TemporaryBRepManager.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns the B-Rep body containing the created wire or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| curves | Curve3D[] | An array containing the input Curve3D objects. These can be Arc3D, Circle3D, Ellipse3D, EllipticalArc3D or Line3D objects. |
| edgeMap | BRepEdge[] | An array of edges in the returned body. The order that the edges are in this collection is the same order as the original corresponding Curve3D object is in the input curves array. This allows you to map between the original input curve and created edge. |
| allowSelfIntersections | boolean | Specifies if you want to allow self-intersection in the input curves or not.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [TemporaryBRepManager API Sample](TemporaryBRepManager_Sample.htm) | TemporaryBRepManager related functions |

## Version

Introduced in version December 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |