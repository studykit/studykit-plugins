# MoveFeatures.createInput Method

Parent Object: [MoveFeatures](MoveFeatures.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MoveFeatures.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method is obsolete. You should use the createInput2 method instead.

## Syntax

* [Python](#Python)
* [C++](#C++)

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.```` ``` returnValue = moveFeatures_var.createInput(inputEntities, transform) ``` ```` |

"moveFeatures\_var" is a variable referencing a [MoveFeatures](MoveFeatures.htm) object.  ```` ``` #include <Fusion/Features/MoveFeatures.h>  returnValue = moveFeatures_var->createInput(inputEntities, transform); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [MoveFeatureInput](MoveFeatureInput.htm) | Returns the newly created MoveFeatureInput object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| inputEntities | [ObjectCollection](ObjectCollection.htm) | An ObjectCollection containing the entities to move. This collection can only contain BRepBody objects in parametric modeling. It can be BRep bodies, T-Spline bodies, mesh bodies mixed or faces and features mixed in non-parametric modeling. |
| transform | [Matrix3D](Matrix3D.htm) | The transform to apply to the input entities. This can describe a move (translation) or a rotation. The matrix must define an orthogonal transform. That is the axes must be perpendicular to each other and there can't be any scaling or mirroring defined. |

## Version

Introduced in version March 2015
Retired in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |