# HoleFeature.setPositionBySketchPoints Method

Parent Object: [HoleFeature](HoleFeature.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Redefines the position and orientation of the hole using a set of points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.```` ``` returnValue = holeFeature_var.setPositionBySketchPoints(sketchPoints) ``` ```` |

"holeFeature\_var" is a variable referencing a [HoleFeature](HoleFeature.htm) object.  ```` ``` #include <Fusion/Features/HoleFeature.h>  returnValue = holeFeature_var->setPositionBySketchPoints(sketchPoints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if successful. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| sketchPoints | [ObjectCollection](ObjectCollection.htm) | A collection of sketch points that defines the positions of the holes. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch. All of the points must be in the same sketch. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |