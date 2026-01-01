# Sketch.sketchCurves Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the sketch curves collection associated with this sketch. This provides access to the existing sketch curves which is all geometry in the sketch except for sketch points. It is through this collection that new sketch geometry gets created.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<SketchCurves> propertyValue = sketch_var->sketchCurves(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchCurves](SketchCurves.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [GeometricConstraint.addMidPont](GeometricConstraint_addMidPont_Sample.htm) | Demonstrate the GeometricConstraint.addMidPont method. |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [SketchArcs.addByCenterStartSweep](SketchArcs_addByCenterStartaSweep_Sample.htm) | Demonstrates the SketchArcs.addByCenterStartSweep method. |
| [SketchArcs.addByThreePoints](SketchArcs_addByThreePoints_Sample.htm) | Demonstrates the SketchArcs.addByThreePoints method. |
| [SketchArcs.addFillet](SketchArcs_addFillet_Sample.htm) | Demonstrates the SketchArcs.addFillet method. |
| [SketchArcs.extend](SketchArcs_extend_Sample.htm) | Demonstrates the SketchArc.extend method. |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |
| [SketchArcs.trim](SketchArcs_trim_Sample.htm) | Demonstrates the SketchArc.trim method. |
| [SketchCircles.addByThreePoints](SketchCircles_addByThreePoints_Sample.htm) | Demonstrates the SketchCircles.addByThreePoints method. |
| [SketchCircles.addByThreeTangents](SketchCircles_addByThreeTangents_Sample.htm) | Demonstrates the SketchCircles.addByThreeTangets method. |
| [SketchCircles.addByTwoPoints](SketchCircles_addByTwoPoints_Sample.htm) | Demonstrates the SketchCircles.addByTwoPoints method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |
| [SketchDimensions.addDiameterDimension](SketchDimension_addDiameterDimension_Sample.htm) | Demonstrates the SketchDimension.addDiameterDimension method. |
| [SketchEllipses.add](SketchEllipses_add_Sample.htm) | Demonstrates the SketchEllipses.add method. |
| [SketchFittedSplines.add](SketchFittedSplines_add_Sample.htm) | Demonstrates the SketchFittedSplines.add method. |
| [SketchFixedSplines.addByNurbsCurve](SketchFixedSplines_addByNurbsCurve_Sample.htm) | Demonstrates the SketchFixedSplines.addByNurbsCurve method. |
| [SketchLines.addDistanceChamfer](SketchLines_addDistanceChamfer_Sample.htm) | Demonstrates the SketchLines.addDistanceChamfer method. |
| [SketchLines.addThreePointRectangle](SketchLines_addThreePointRectangle_Sample.htm) | Demonstrates the SketchLines.addThreePointRectangle method. |
| [SketchLines.addTwoPointRectangle](SketchLines_addTwoPointRectangle_Sample.htm) | Demonstrates the SketchLines.addTwoPointRectangle method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |