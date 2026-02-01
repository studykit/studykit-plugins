# ConstructionPlaneTangentDefinition.redefine Method

Parent Object: [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneTangentDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneTangentDefinition\_var" is a variable referencing a [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm) object.```` ``` returnValue = constructionPlaneTangentDefinition_var.redefine(angle, tangentFace, planarEntity) ``` ```` |

"constructionPlaneTangentDefinition\_var" is a variable referencing a [ConstructionPlaneTangentDefinition](ConstructionPlaneTangentDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| angle | [ValueInput](ValueInput.htm) | A Value object that defines the angle of the construction plane |
| tangentFace | [Base](Base.htm) | The cylindrical or conical face that the construction plane is tangent to. |
| planarEntity | [Base](Base.htm) | The planar face or construction plane the angle for this construction plane is measured from |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |