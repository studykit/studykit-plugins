# ConstructionPoints.add Method

Parent Object: [ConstructionPoints](ConstructionPoints.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPoints.h>

## Description

Creates a new construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.```` ``` returnValue = constructionPoints_var.add(input) ``` ```` |

"constructionPoints\_var" is a variable referencing a [ConstructionPoints](ConstructionPoints.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionPoints.h>  returnValue = constructionPoints_var->add(input); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConstructionPoint](ConstructionPoint.htm) | Returns the newly created construction point or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| input | [ConstructionPointInput](ConstructionPointInput.htm) | A ConstructionPointInput object |

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