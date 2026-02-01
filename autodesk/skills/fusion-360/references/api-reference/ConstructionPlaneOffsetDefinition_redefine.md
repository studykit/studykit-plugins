# ConstructionPlaneOffsetDefinition.redefine Method

Parent Object: [ConstructionPlaneOffsetDefinition](ConstructionPlaneOffsetDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneOffsetDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneOffsetDefinition\_var" is a variable referencing a [ConstructionPlaneOffsetDefinition](ConstructionPlaneOffsetDefinition.htm) object.```` ``` returnValue = constructionPlaneOffsetDefinition_var.redefine(offset, planarEntity) ``` ```` |

"constructionPlaneOffsetDefinition\_var" is a variable referencing a [ConstructionPlaneOffsetDefinition](ConstructionPlaneOffsetDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is the operation is successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| offset | [ValueInput](ValueInput.htm) | ValueInput object that specifies the offset distance |
| planarEntity | [Base](Base.htm) | A plane, planar face or construction plane from which to measure the offset from |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |