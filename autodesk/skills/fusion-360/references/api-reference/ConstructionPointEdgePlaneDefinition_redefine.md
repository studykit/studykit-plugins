# ConstructionPointEdgePlaneDefinition.redefine Method

Parent Object: [ConstructionPointEdgePlaneDefinition](ConstructionPointEdgePlaneDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPointEdgePlaneDefinition.h>

## Description

Redefines the input geometry of the construction point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPointEdgePlaneDefinition\_var" is a variable referencing a [ConstructionPointEdgePlaneDefinition](ConstructionPointEdgePlaneDefinition.htm) object.```` ``` returnValue = constructionPointEdgePlaneDefinition_var.redefine(edge, plane) ``` ```` |

"constructionPointEdgePlaneDefinition\_var" is a variable referencing a [ConstructionPointEdgePlaneDefinition](ConstructionPointEdgePlaneDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition of the Construction Point is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| edge | [Base](Base.htm) | A linear B-Rep edge, construction axis or sketch line. |
| plane | [Base](Base.htm) | A plane, planar B-Rep face or construction plane. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |