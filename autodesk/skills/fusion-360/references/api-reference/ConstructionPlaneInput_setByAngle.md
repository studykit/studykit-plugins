# ConstructionPlaneInput.setByAngle Method

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

This input method is for creating a construction plane through an edge, axis or line at a specified angle. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object.```` ``` returnValue = constructionPlaneInput_var.setByAngle(linearEntity, angle, planarEntity) ``` ```` |

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
| linearEntity | [Base](Base.htm) | The axis about which to rotate the plane |
| angle | [ValueInput](ValueInput.htm) | The angle at which to create the plane |
| planarEntity | [Base](Base.htm) | The planar face or construction plane the angle is measured from. |

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