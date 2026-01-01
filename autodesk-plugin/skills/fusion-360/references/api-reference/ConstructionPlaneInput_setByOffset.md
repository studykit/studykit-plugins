# ConstructionPlaneInput.setByOffset Method

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

This input method is for creating a construction plane that is offset from a planar face or construction plane at a specified distance. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object.```` ``` returnValue = constructionPlaneInput_var.setByOffset(planarEntity, offset) ``` ```` |

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
| planarEntity | [Base](Base.htm) | A plane, planar face or construction plane from which to create the offset plane |
| offset | [ValueInput](ValueInput.htm) | ValueInput object that specifies the offset distance for the plane |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |