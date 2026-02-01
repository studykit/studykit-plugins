# ConstructionPlaneTangentAtPointDefinition.redefine Method

Parent Object: [ConstructionPlaneTangentAtPointDefinition](ConstructionPlaneTangentAtPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentAtPointDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneTangentAtPointDefinition\_var" is a variable referencing a [ConstructionPlaneTangentAtPointDefinition](ConstructionPlaneTangentAtPointDefinition.htm) object.```` ``` returnValue = constructionPlaneTangentAtPointDefinition_var.redefine(tangentFace, pointEntity) ``` ```` |

"constructionPlaneTangentAtPointDefinition\_var" is a variable referencing a [ConstructionPlaneTangentAtPointDefinition](ConstructionPlaneTangentAtPointDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| tangentFace | [Base](Base.htm) | The face to create the plane tangent to |
| pointEntity | [Base](Base.htm) | The point (sketch point, vertex, construction point) used to align the plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |