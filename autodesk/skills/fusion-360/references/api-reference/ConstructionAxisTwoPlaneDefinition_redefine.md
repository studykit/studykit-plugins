# ConstructionAxisTwoPlaneDefinition.redefine Method

Parent Object: [ConstructionAxisTwoPlaneDefinition](ConstructionAxisTwoPlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisTwoPlaneDefinition.h>

## Description

Redefines the input geometry of the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisTwoPlaneDefinition\_var" is a variable referencing a [ConstructionAxisTwoPlaneDefinition](ConstructionAxisTwoPlaneDefinition.htm) object.```` ``` returnValue = constructionAxisTwoPlaneDefinition_var.redefine(planarEntityOne, planarEntityTwo) ``` ```` |

"constructionAxisTwoPlaneDefinition\_var" is a variable referencing a [ConstructionAxisTwoPlaneDefinition](ConstructionAxisTwoPlaneDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the axis is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntityOne | [Base](Base.htm) | The first planar face or construction plane |
| planarEntityTwo | [Base](Base.htm) | The second planar face or construction plane |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |