# ConstructionAxisPerpendicularAtPointDefinition.redefine Method

Parent Object: [ConstructionAxisPerpendicularAtPointDefinition](ConstructionAxisPerpendicularAtPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisPerpendicularAtPointDefinition.h>

## Description

Redefines the input geometry of the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisPerpendicularAtPointDefinition\_var" is a variable referencing a [ConstructionAxisPerpendicularAtPointDefinition](ConstructionAxisPerpendicularAtPointDefinition.htm) object.```` ``` returnValue = constructionAxisPerpendicularAtPointDefinition_var.redefine(face, pointEntity) ``` ```` |

"constructionAxisPerpendicularAtPointDefinition\_var" is a variable referencing a [ConstructionAxisPerpendicularAtPointDefinition](ConstructionAxisPerpendicularAtPointDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the axis is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [BRepFace](BRepFace.htm) | The face (BRepFace object) to create the axis perpendicular to. |
| pointEntity | [Base](Base.htm) | The point (sketch point, vertex, construction point) used to position the axis. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |