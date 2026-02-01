# ConstructionPointInput.setByPoint Method

Parent Object: [ConstructionPointInput](ConstructionPointInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointInput.h>

## Description

This input method is for creating a construction point on the specified point or vertex. The point can be either a B-Rep vertex, SketchPoint, or a Point3D object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointInput\_var" is a variable referencing a [ConstructionPointInput](ConstructionPointInput.htm) object.```` ``` returnValue = constructionPointInput_var.setByPoint(point) ``` ```` |

"constructionPointInput\_var" is a variable referencing a [ConstructionPointInput](ConstructionPointInput.htm) object.  ```` ``` #include <Fusion/Construction/ConstructionPointInput.h>  returnValue = constructionPointInput_var->setByPoint(point); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionPointInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| point | [Base](Base.htm) | A B-Rep vertex, SketchPoint, or Point object |

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