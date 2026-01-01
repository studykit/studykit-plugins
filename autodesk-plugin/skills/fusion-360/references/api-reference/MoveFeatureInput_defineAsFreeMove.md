# MoveFeatureInput.defineAsFreeMove Method

Parent Object: [MoveFeatureInput](MoveFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatureInput.h>

## Description

This method will define a move feature whose translation and orientation is defined using a transformation matrix. A matrix can define any translation and orientation.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatureInput\_var" is a variable referencing a [MoveFeatureInput](MoveFeatureInput.htm) object.```` ``` returnValue = moveFeatureInput_var.defineAsFreeMove(transform) ``` ```` |

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
| transform | [Matrix3D](Matrix3D.htm) | The transformation matrix that defines the transform to apply. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Move Feature API Sample](MoveFeatureSample_Sample.htm) | Demonstrates creating a new move feature. |

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |