# SketchArc.split Method

Parent Object: [SketchArc](SketchArc.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchArc.h>

## Description

Split a curve at a position specified along the curve

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchArc\_var" is a variable referencing a [SketchArc](SketchArc.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"sketchArc\_var" is a variable referencing a [SketchArc](SketchArc.htm) object.  ```` ``` #include <Fusion/Sketch/SketchArc.h>  // Uses no optional arguments. returnValue = sketchArc_var->split(splitPoint);  // Uses optional arguments. returnValue = sketchArc_var->split(splitPoint, createConstraints); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ObjectCollection](ObjectCollection.htm) | Returns the resulting 2 curves; the original curve + the newly created curve When split spline the original is deleted and two new curves returned. Empty collection returned if curve is closed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| splitPoint | [Point3D](Point3D.htm) | A position (transient Point3D) on the curve that defines the point at which to split the curve |
| createConstraints | boolean | Constraints are created by default. Specify false to create no constraints.   This is an optional argument whose default value is True. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |