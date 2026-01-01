# ConstructionPlaneThreePointsDefinition.redefine Method

Parent Object: [ConstructionPlaneThreePointsDefinition](ConstructionPlaneThreePointsDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneThreePointsDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneThreePointsDefinition\_var" is a variable referencing a [ConstructionPlaneThreePointsDefinition](ConstructionPlaneThreePointsDefinition.htm) object.```` ``` returnValue = constructionPlaneThreePointsDefinition_var.redefine(pointEntityOne, pointEntityTwo, pointEntityThree) ``` ```` |

"constructionPlaneThreePointsDefinition\_var" is a variable referencing a [ConstructionPlaneThreePointsDefinition](ConstructionPlaneThreePointsDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the plane is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointEntityOne | [Base](Base.htm) | Gets the first construction point, sketch point or vertex. |
| pointEntityTwo | [Base](Base.htm) | Gets the second construction point, sketch point or vertex. |
| pointEntityThree | [Base](Base.htm) | Gets the third construction point, sketch point or vertex. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |