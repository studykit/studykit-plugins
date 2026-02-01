# MoveFeature.redefineAsRotate Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Redefines the move feature to be described by an axis and rotation angle.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.redefineAsRotate(axisEntity, angle) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.  ```` ``` #include <Fusion/Features/MoveFeature.h>  returnValue = moveFeature_var->redefineAsRotate(axisEntity, angle); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| axisEntity | [Base](Base.htm) | A linear entity that defines the axis of rotation. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The natural direction of the entity defines a right-hand rule for the rotation direction. |
| angle | [ValueInput](ValueInput.htm) | A ValueInput object that defines the rotation angle. If the ValueInput is created using a real value, the angle is in radians. If it's defined using a string, the default document units will be used. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |