# ConstructionAxisTwoPointDefinition.redefine Method

Parent Object: [ConstructionAxisTwoPointDefinition](ConstructionAxisTwoPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisTwoPointDefinition.h>

## Description

Redefines the input geometry of the construction axis.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisTwoPointDefinition\_var" is a variable referencing a [ConstructionAxisTwoPointDefinition](ConstructionAxisTwoPointDefinition.htm) object.```` ``` returnValue = constructionAxisTwoPointDefinition_var.redefine(pointEntityOne, pointEntityTwo) ``` ```` |

"constructionAxisTwoPointDefinition\_var" is a variable referencing a [ConstructionAxisTwoPointDefinition](ConstructionAxisTwoPointDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the construction axis is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| pointEntityOne | [Base](Base.htm) | The first point |
| pointEntityTwo | [Base](Base.htm) | The second point |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |