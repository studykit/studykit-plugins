# ConstructionAxisNormalToFaceAtPointDefinition.redefine Method

Parent Object: [ConstructionAxisNormalToFaceAtPointDefinition](ConstructionAxisNormalToFaceAtPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisNormalToFaceAtPointDefinition.h>

## Description

Redefines the input geometry of the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisNormalToFaceAtPointDefinition\_var" is a variable referencing a [ConstructionAxisNormalToFaceAtPointDefinition](ConstructionAxisNormalToFaceAtPointDefinition.htm) object.```` ``` returnValue = constructionAxisNormalToFaceAtPointDefinition_var.redefine(face, pointEntity) ``` ```` |

"constructionAxisNormalToFaceAtPointDefinition\_var" is a variable referencing a [ConstructionAxisNormalToFaceAtPointDefinition](ConstructionAxisNormalToFaceAtPointDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the construction axis is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [Base](Base.htm) | The face the axis is normal to |
| pointEntity | [Base](Base.htm) | The point that positions the axis |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |