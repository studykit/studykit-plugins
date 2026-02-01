# ConstructionPointThreePlanesDefinition.redefine Method

Parent Object: [ConstructionPointThreePlanesDefinition](ConstructionPointThreePlanesDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointThreePlanesDefinition.h>

## Description

Redefines the input geometry of the construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointThreePlanesDefinition\_var" is a variable referencing a [ConstructionPointThreePlanesDefinition](ConstructionPointThreePlanesDefinition.htm) object.```` ``` returnValue = constructionPointThreePlanesDefinition_var.redefine(planeOne, planeTwo, planeThree) ``` ```` |

"constructionPointThreePlanesDefinition\_var" is a variable referencing a [ConstructionPointThreePlanesDefinition](ConstructionPointThreePlanesDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the Construction Point is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planeOne | [Base](Base.htm) | The first plane or planar face to intersect |
| planeTwo | [Base](Base.htm) | The second plane or planar face to intersect |
| planeThree | [Base](Base.htm) | The third plane or planar face to intersect |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |