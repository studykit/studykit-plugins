# ConstructionPlaneMidplaneDefinition.redefine Method

Parent Object: [ConstructionPlaneMidplaneDefinition](ConstructionPlaneMidplaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneMidplaneDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneMidplaneDefinition\_var" is a variable referencing a [ConstructionPlaneMidplaneDefinition](ConstructionPlaneMidplaneDefinition.htm) object.```` ``` returnValue = constructionPlaneMidplaneDefinition_var.redefine(planarEntityOne, planarEntityTwo) ``` ```` |

"constructionPlaneMidplaneDefinition\_var" is a variable referencing a [ConstructionPlaneMidplaneDefinition](ConstructionPlaneMidplaneDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntityOne | [Base](Base.htm) | The first planar face or construction plane that defines this ConstructionPlane. |
| planarEntityTwo | [Base](Base.htm) | The second planar face or construction plane that defines this ConstructionPlane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |