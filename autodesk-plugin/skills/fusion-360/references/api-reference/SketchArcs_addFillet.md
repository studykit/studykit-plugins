# SketchArcs.addFillet Method

Parent Object: [SketchArcs](SketchArcs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArcs.h>

## Description

Creates a fillet between two sketch entities The side (quadrant) the fillet is created on is determined by the points specified. The point for each entity can be its startSketchPoint or endSketchPoint

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object.```` ``` returnValue = sketchArcs_var.addFillet(firstEntity, firstEntityPoint, secondEnitity, secondEntityPoint, radius) ``` ```` |

"sketchArcs\_var" is a variable referencing a [SketchArcs](SketchArcs.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [SketchArc](SketchArc.htm) | Returns the newly created SketchArc object (fillet) if the operation was successful or null if it failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| firstEntity | [SketchCurve](SketchCurve.htm) | The first curve for the fillet definition. The curve must be open. |
| firstEntityPoint | [Point3D](Point3D.htm) | A point on or closer to one end of the first curve that indicates the side to create the fillet on |
| secondEnitity | [SketchCurve](SketchCurve.htm) | The second curve for the fillet definition. The curve must be open. |
| secondEntityPoint | [Point3D](Point3D.htm) | A point on or closer to one end of the second curve that indicates the side to create the fillet on |
| radius | double | radius of the arc in centimeters |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch fillet and offset API Sample](SketchFilletAndOffset_Sample.htm) | Demonstrates the creation of a fillet in a sketch and offset a set of curves. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |