# MoveFeature.redefineAsFreeMove Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Redefines the move feature to be described by an arbitrary translation and orientation which is defined using a transformation matrix.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.redefineAsFreeMove(transform) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.  ```` ``` #include <Fusion/Features/MoveFeature.h>  returnValue = moveFeature_var->redefineAsFreeMove(transform); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the re-definition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| transform | [Matrix3D](Matrix3D.htm) | The transformation matrix that defines the transform to apply. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |