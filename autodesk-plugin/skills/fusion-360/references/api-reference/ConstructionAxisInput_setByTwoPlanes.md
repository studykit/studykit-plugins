# ConstructionAxisInput.setByTwoPlanes Method

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

This input method is for creating a construction axis coincident with the intersection of two planes or planar faces. This will fail if the two planes are parallel. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object.```` ``` returnValue = constructionAxisInput_var.setByTwoPlanes(planarEntityOne, planarEntityTwo) ``` ```` |

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionAxisInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntityOne | [Base](Base.htm) | The first planar face or construction plane to intersect |
| planarEntityTwo | [Base](Base.htm) | The second planar face or construction plane to intersect |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |