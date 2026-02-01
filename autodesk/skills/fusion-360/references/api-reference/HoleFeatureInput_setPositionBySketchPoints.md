# HoleFeatureInput.setPositionBySketchPoints Method

Parent Object: [HoleFeatureInput](HoleFeatureInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeatureInput.h>

## Description

Defines the position and orientation of the hole using a set of sketch points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object.```` ``` returnValue = holeFeatureInput_var.setPositionBySketchPoints(sketchPoints) ``` ```` |

"holeFeatureInput\_var" is a variable referencing a [HoleFeatureInput](HoleFeatureInput.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchPoints | [ObjectCollection](ObjectCollection.htm) | A collection of sketch points that defines the positions of the holes. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch. The points can be from multiple sketches but they must all be co-planar. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole Feature API Sample](HoleFeatureSample_Sample.htm) | Demonstrates creating a new hole feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |