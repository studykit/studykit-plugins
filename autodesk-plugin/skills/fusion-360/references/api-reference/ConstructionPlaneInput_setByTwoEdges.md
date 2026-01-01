# ConstructionPlaneInput.setByTwoEdges Method

Parent Object: [ConstructionPlaneInput](ConstructionPlaneInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneInput.h>

## Description

This input method is for creating a construction plane that passes through two coplanar linear entities or axes. Defines a plane by specifying two coplanar linear entities. This can result in a parametric or non-parametric construction plane depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object.```` ``` returnValue = constructionPlaneInput_var.setByTwoEdges(linearEntityOne, linearEntityTwo) ``` ```` |

"constructionPlaneInput\_var" is a variable referencing a [ConstructionPlaneInput](ConstructionPlaneInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionPlaneInput is successful. This will fail if the two linear entities are not coplanar. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| linearEntityOne | [Base](Base.htm) | The first of two coplanar linear entities to define the plane |
| linearEntityTwo | [Base](Base.htm) | The second of two coplanar linear entities to define the plane |

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