# ConstructionAxisInput.setByPerpendicularAtPoint Method

Parent Object: [ConstructionAxisInput](ConstructionAxisInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxisInput.h>

## Description

This input method is for creating an axis that is normal to a face at a specified point.

## Syntax

* [Python](#Python)
* [C++](#C++)

"constructionAxisInput\_var" is a variable referencing a [ConstructionAxisInput](ConstructionAxisInput.htm) object.```` ``` returnValue = constructionAxisInput_var.setByPerpendicularAtPoint(face, pointEntity) ``` ```` |

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
| face | [BRepFace](BRepFace.htm) | A face (BRepFace object) to create the axis normal to. |
| pointEntity | [Base](Base.htm) | A construction point, sketch point or vertex the axis is to pass through. |

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