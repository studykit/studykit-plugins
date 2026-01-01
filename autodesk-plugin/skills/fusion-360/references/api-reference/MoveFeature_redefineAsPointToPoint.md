# MoveFeature.redefineAsPointToPoint Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Redefines the move feature to be a translation from one point to another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.redefineAsPointToPoint(originPoint, targetPoint) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.  ```` ``` #include <Fusion/Features/MoveFeature.h>  returnValue = moveFeature_var->redefineAsPointToPoint(originPoint, targetPoint); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| originPoint | [Base](Base.htm) | The first point that defines the start position of the move. |
| targetPoint | [Base](Base.htm) | The second point that defines the direction and distance of the move. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |