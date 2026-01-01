# SketchCurves.sketchLines Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch lines collection associated with this sketch. This provides access to the existing sketch lines and supports the creation of new sketch lines.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchLines> propertyValue = sketchCurves_var->sketchLines(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchLines](SketchLines.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [SketchCircles.addByThreeTangents](SketchCircles_addByThreeTangents_Sample.htm) | Demonstrates the SketchCircles.addByThreeTangets method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |
| [SketchLines.addAngleChamfer](SketchLines_addAngleChamfer_Sample.htm) | Demonstrates the SketchLines.addAngleChamfer method. |
| [SketchLines.addByTwoPoints](SketchLines_addByTwoPoints_Sample.htm) | Demonstrates the SketchLines.addByTwoPoints method. |
| [SketchLines.addCenterPointRectangle](SketchLines_addCenterPointRectangle_Sample.htm) | Demonstrates the SketchLines.addCenterPointRectangle method. |
| [SketchLines.addDistanceChamfer](SketchLines_addDistanceChamfer_Sample.htm) | Demonstrates the SketchLines.addDistanceChamfer method. |
| [SketchLines.addThreePointRectangle](SketchLines_addThreePointRectangle_Sample.htm) | Demonstrates the SketchLines.addThreePointRectangle method. |
| [SketchLines.addTwoPointRectangle](SketchLines_addTwoPointRectangle_Sample.htm) | Demonstrates the SketchLines.addTwoPointRectangle method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |