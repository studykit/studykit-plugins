# ConstructionPlaneInput.setByTangent Method

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

This input method is for creating a construction plane tangent to a cylindrical or conical face at a specified point. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object.```` ``` returnValue = constructionPlaneInput_var.setByTangent(tangentFace, angle, planarEntity) ``` ```` |

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionPlaneInput is successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tangentFace | [BRepFace](BRepFace.htm) | A cylindrical or conical face to create the plane tangent to |
| angle | [ValueInput](ValueInput.htm) | The angle relative to the planarEntity input at which to create the tangent plane |
| planarEntity | [Base](Base.htm) | The planar face or construction plane the tangent is measured from. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |