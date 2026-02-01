# MoveFeature.redefineAsTranslateAlongEntity Method

Parent Object: [MoveFeature](MoveFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeature.h>

## Description

Redefines the move feature to be a translation along a specified entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.```` ``` returnValue = moveFeature_var.redefineAsTranslateAlongEntity(linearEntity, distance) ``` ```` |

"moveFeature\_var" is a variable referencing a [MoveFeature](MoveFeature.htm) object.  ```` ``` #include <Fusion/Features/MoveFeature.h>  returnValue = moveFeature_var->redefineAsTranslateAlongEntity(linearEntity, distance); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the redefinition is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| linearEntity | [Base](Base.htm) | A linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction. |
| distance | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset distance. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |