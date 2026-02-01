# ConstructionPlaneTwoEdgesDefinition.redefine Method

Parent Object: [ConstructionPlaneTwoEdgesDefinition](ConstructionPlaneTwoEdgesDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTwoEdgesDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneTwoEdgesDefinition\_var" is a variable referencing a [ConstructionPlaneTwoEdgesDefinition](ConstructionPlaneTwoEdgesDefinition.htm) object.```` ``` returnValue = constructionPlaneTwoEdgesDefinition_var.redefine(linearEntityOne, linearEntityTwo) ``` ```` |

"constructionPlaneTwoEdgesDefinition\_var" is a variable referencing a [ConstructionPlaneTwoEdgesDefinition](ConstructionPlaneTwoEdgesDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| linearEntityOne | [Base](Base.htm) | The first linear edge, construction line, or sketch line that defines the construction plane. |
| linearEntityTwo | [Base](Base.htm) | The second linear edge, construction line, or sketch line that defines the construction plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |