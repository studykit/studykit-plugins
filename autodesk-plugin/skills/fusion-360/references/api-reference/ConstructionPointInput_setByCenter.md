# ConstructionPointInput.setByCenter Method

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

This input method is for creating a construction point at the center of a spherical face (sphere or torus), circular edge or sketch arc/circle This can result in a parametric or non-parametric construction point depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a [ConstructionPointInput](ConstructionPointInput.htm) object.```` ``` returnValue = constructionPointInput_var.setByCenter(circularEntity) ``` ```` |

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
| circularEntity | [Base](Base.htm) | A spherical face (sphere or torus), circular edge or sketch arc/circle |

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