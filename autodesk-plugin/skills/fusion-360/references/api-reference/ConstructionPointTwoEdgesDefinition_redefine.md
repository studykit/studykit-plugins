# ConstructionPointTwoEdgesDefinition.redefine Method

Parent Object: [ConstructionPointTwoEdgesDefinition](ConstructionPointTwoEdgesDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointTwoEdgesDefinition.h>

## Description

Redefines the input geometry of the construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointTwoEdgesDefinition\_var" is a variable referencing a [ConstructionPointTwoEdgesDefinition](ConstructionPointTwoEdgesDefinition.htm) object.```` ``` returnValue = constructionPointTwoEdgesDefinition_var.redefine(edgeOne, edgeTwo) ``` ```` |

"constructionPointTwoEdgesDefinition\_var" is a variable referencing a [ConstructionPointTwoEdgesDefinition](ConstructionPointTwoEdgesDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the Construction Point is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edgeOne | [Base](Base.htm) | The first B-Rep edge or sketch line |
| edgeTwo | [Base](Base.htm) | The second B-Rep edge or sketch line |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |