# ConstructionPlanes.add Method

Parent Object: [ConstructionPlanes](ConstructionPlanes.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlanes.h>

## Description

Creates and adds a new ConstructionPlane using the creation parameters in the ConstructionPlaneInput.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.```` ``` returnValue = constructionPlanes_var.add(input) ``` ```` |

"constructionPlanes\_var" is a variable referencing a [ConstructionPlanes](ConstructionPlanes.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionPlanes.h>  returnValue = constructionPlanes_var->add(input); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPlane](ConstructionPlane.htm) | Returns the newly created construction plane or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ConstructionPlaneInput](ConstructionPlaneInput.htm) | A ConstructionPlaneInput object |

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