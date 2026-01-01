# TemporaryBRepManager.createProjectedBodyOutline Method

Parent Object: [TemporaryBRepManager](TemporaryBRepManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/TemporaryBRepManager.h>

## Description

Computes the approximate outline of a body. The outline is the loops formed from projecting the non-occluded silhouette curves of the body onto a plane. The outline is returned as a temporary BRepBody consisting of planar BRepFace objects whose boundaries form the outline.

## Syntax

* [Python](#Python)
* [C++](#C++)

"temporaryBRepManager\_var" is a variable referencing a [TemporaryBRepManager](TemporaryBRepManager.htm) object.  ```` ``` (returnValue, containsApproximation) = temporaryBRepManager_var.createProjectedBodyOutline(body, projectionPlane, tolerance) ``` ```` |

```` ```  #include <Fusion/BRep/TemporaryBRepManager.h ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [BRepBody](BRepBody.htm) | Returns a BRepBody object consisting of planar BRepFace objects whose boundaries define the body's outline. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| body | [BRepBody](BRepBody.htm) | Input BRepBody object to calculate the projected outline for. |
| projectionPlane | [Plane](Plane.htm) | Input Plane object that defines the position and orientation of the plane to project the body onto. The resulting body will lie on this plane. |
| tolerance | double | Input value that specifies the tolerance in centimeters to use when approximating smooth surfaces with line segments. A negative tolerance uses the default value which is 0.001 times the length of the diagonal of the bounding box of the input body. A positive tolerance must be greater than the point tolerance (0.000001). |
| containsApproximation | boolean | Output value that indicates if the result contains any silhouette curves that are an approximation of the true silhouette. |

## Version

Introduced in version November 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |