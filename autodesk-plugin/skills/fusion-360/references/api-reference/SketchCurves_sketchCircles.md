# SketchCurves.sketchCircles Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch circles collection associated with this sketch. This provides access to the existing sketch circles and supports the creation of new sketch circles.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchCircles> propertyValue = sketchCurves_var->sketchCircles(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchCircles](SketchCircles.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create circle by center and radius API Sample](CircleByCenterRadius_Sample.htm) | Demonstrates creating a sketch circle by the center and radius. |
| [GeometricConstraint.addMidPont](GeometricConstraint_addMidPont_Sample.htm) | Demonstrate the GeometricConstraint.addMidPont method. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [SketchCircles.addByCenterRadius](SketchCircles_addByCenterRadius_Sample.htm) | Demonstrates the SketchCircles.addByCenterRadius method. |
| [SketchCircles.addByThreePoints](SketchCircles_addByThreePoints_Sample.htm) | Demonstrates the SketchCircles.addByThreePoints method. |
| [SketchCircles.addByThreeTangents](SketchCircles_addByThreeTangents_Sample.htm) | Demonstrates the SketchCircles.addByThreeTangets method. |
| [SketchCircles.addByTwoPoints](SketchCircles_addByTwoPoints_Sample.htm) | Demonstrates the SketchCircles.addByTwoPoints method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |