# ConstructionPlaneInput.setByDistanceOnPath Method

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

This input method is for creating a construction plane normal to, and at specified distance along, a path defined by an edge or sketch profile. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object.```` ``` returnValue = constructionPlaneInput_var.setByDistanceOnPath(pathEntity, distance) ``` ```` |

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionPlaneInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pathEntity | [Base](Base.htm) | The path can be an edge, sketch curve, or a path of multiple entities. |
| distance | [ValueInput](ValueInput.htm) | The distance is a value from 0 to 1 indicating the position along the path where 0 is at the start and 1 is at the end. |

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