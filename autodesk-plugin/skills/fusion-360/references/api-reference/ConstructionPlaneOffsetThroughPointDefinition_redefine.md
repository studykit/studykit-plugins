# ConstructionPlaneOffsetThroughPointDefinition.redefine Method

Parent Object: [ConstructionPlaneOffsetThroughPointDefinition](ConstructionPlaneOffsetThroughPointDefinition.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlaneOffsetThroughPointDefinition.h>

## Description

Redefines the input geometry of the construction plane.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionPlaneOffsetThroughPointDefinition\_var" is a variable referencing a [ConstructionPlaneOffsetThroughPointDefinition](ConstructionPlaneOffsetThroughPointDefinition.htm) object.```` ``` returnValue = constructionPlaneOffsetThroughPointDefinition_var.redefine(planarEntity, point) ``` ```` |

"constructionPlaneOffsetThroughPointDefinition\_var" is a variable referencing a [ConstructionPlaneOffsetThroughPointDefinition](ConstructionPlaneOffsetThroughPointDefinition.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is the operation is successful |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| planarEntity | [Base](Base.htm) | A planar BRepFace or ConstructionPlane that the new construction plane will be offset from. |
| point | [Base](Base.htm) | A BRepVertex, SketchPoint, or ConstructionPoint that defines the offset distance. |

## Version

Introduced in version January 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |