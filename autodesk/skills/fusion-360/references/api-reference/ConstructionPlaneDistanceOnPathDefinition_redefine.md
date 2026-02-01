# ConstructionPlaneDistanceOnPathDefinition.redefine Method

Parent Object: [ConstructionPlaneDistanceOnPathDefinition](ConstructionPlaneDistanceOnPathDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneDistanceOnPathDefinition.h>

## Description

Redefines the input defining the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneDistanceOnPathDefinition\_var" is a variable referencing a [ConstructionPlaneDistanceOnPathDefinition](ConstructionPlaneDistanceOnPathDefinition.htm) object.```` ``` returnValue = constructionPlaneDistanceOnPathDefinition_var.redefine(pathEntity, distance) ``` ```` |

"constructionPlaneDistanceOnPathDefinition\_var" is a variable referencing a [ConstructionPlaneDistanceOnPathDefinition](ConstructionPlaneDistanceOnPathDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pathEntity | [Base](Base.htm) | The sketch curve, edge, or a profile object |
| distance | [ValueInput](ValueInput.htm) | The ValueInput object that defines the distance along the path |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |