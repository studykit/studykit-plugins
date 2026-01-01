# ConstructionAxisInput.setByNormalToFaceAtPoint Method

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

This input method if for creating a construction axis normal to a specified face or sketch profile and that passes through a specified point. This can result in a parametric or non-parametric construction axis depending on whether the parent component is parametric or is a direct edit component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object.```` ``` returnValue = constructionAxisInput_var.setByNormalToFaceAtPoint(face, pointEntity) ``` ```` |

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the creation of the ConstructionAxisInput is successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| face | [BRepFace](BRepFace.htm) | The face (BRepFace object) to create the axis normal to. |
| pointEntity | [Base](Base.htm) | A construction point, sketch point or vertex the axis passes through. This point does not have to lie on the face. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |