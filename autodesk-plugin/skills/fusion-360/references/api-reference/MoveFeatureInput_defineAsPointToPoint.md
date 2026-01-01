# MoveFeatureInput.defineAsPointToPoint Method

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

This method defines a move feature described by a translation from one point to another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a [MoveFeatureInput](MoveFeatureInput.htm) object.```` ``` returnValue = moveFeatureInput_var.defineAsPointToPoint(originPoint, targetPoint) ``` ```` |

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
| originPoint | [Base](Base.htm) | The first point that defines the start position of the move. |
| targetPoint | [Base](Base.htm) | The second point that defines the direction and distance of the move. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |