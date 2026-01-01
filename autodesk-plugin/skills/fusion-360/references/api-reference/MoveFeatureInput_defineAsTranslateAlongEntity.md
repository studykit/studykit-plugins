# MoveFeatureInput.defineAsTranslateAlongEntity Method

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

This method will define a move feature that defines a translation along a specified entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a [MoveFeatureInput](MoveFeatureInput.htm) object.```` ``` returnValue = moveFeatureInput_var.defineAsTranslateAlongEntity(linearEntity, distance) ``` ```` |

"moveFeatureInput\_var" is a variable referencing a [MoveFeatureInput](MoveFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if defining the type of move is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| linearEntity | [Base](Base.htm) | A linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction. |
| distance | [ValueInput](ValueInput.htm) | A ValueInput object that defines the offset distance. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units are used. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |