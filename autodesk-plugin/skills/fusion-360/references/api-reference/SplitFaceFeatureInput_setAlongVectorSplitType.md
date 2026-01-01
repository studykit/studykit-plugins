# SplitFaceFeatureInput.setAlongVectorSplitType Method

Parent Object: [SplitFaceFeatureInput](SplitFaceFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/SplitFaceFeatureInput.h>

## Description

Sets the split type to project the splitting tool along the direction defined by the specified entity.

## Syntax

* [Python](#Python)
* [C++](#C++)

"splitFaceFeatureInput\_var" is a variable referencing a [SplitFaceFeatureInput](SplitFaceFeatureInput.htm) object.```` ``` returnValue = splitFaceFeatureInput_var.setAlongVectorSplitType(directionEntity) ``` ```` |

"splitFaceFeatureInput\_var" is a variable referencing a [SplitFaceFeatureInput](SplitFaceFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true is setting the split type was successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| directionEntity | [Base](Base.htm) | An entity that defines the direction of projection of the splitting tool. This can be a linear BRepEdge, SketchLine, ConstructionLine, or a planar face where the face normal is used. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Split Face Feature API Sample](SplitFaceFeatureSample_Sample.htm) | Demonstrates creating a new split face feature. |

## Version

Introduced in version May 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |