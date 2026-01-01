# ConstructionPointInput.setByEdgePlane Method

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

This input method is for creating a construction point at the intersection of a construction plane, planar face or sketch profile and a linear edge, construction axis or sketch line. This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a [ConstructionPointInput](ConstructionPointInput.htm) object.```` ``` returnValue = constructionPointInput_var.setByEdgePlane(edge, plane) ``` ```` |

"constructionPointInput\_var" is a variable referencing a [ConstructionPointInput](ConstructionPointInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionPointInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edge | [Base](Base.htm) | A linear B-Rep edge, construction axis or sketch line. |
| plane | [Base](Base.htm) | A plane, planar B-Rep face or construction plane. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Point API Sample](ConstructionPointSample_Sample.htm) | Demonstrates creating construction point by different ways |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |