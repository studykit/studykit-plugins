# SketchCurves.sketchArcs Property

Parent Object: [SketchCurves](SketchCurves.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchCurves.h>

## Description

Returns the sketch arcs collection associated with this sketch. This provides access to the existing sketch arcs and supports the creation of new sketch arcs.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchCurves\_var" is a variable referencing a SketchCurves object. |

"sketchCurves\_var" is a variable referencing a SketchCurves object. ```` ``` #include <Fusion/Sketch/SketchCurves.h>  // Get the value of the property. Ptr<SketchArcs> propertyValue = sketchCurves_var->sketchArcs(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchArcs](SketchArcs.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [SketchArcs.addByCenterStartSweep](SketchArcs_addByCenterStartaSweep_Sample.htm) | Demonstrates the SketchArcs.addByCenterStartSweep method. |
| [SketchArcs.addByThreePoints](SketchArcs_addByThreePoints_Sample.htm) | Demonstrates the SketchArcs.addByThreePoints method. |
| [SketchArcs.addFillet](SketchArcs_addFillet_Sample.htm) | Demonstrates the SketchArcs.addFillet method. |
| [SketchArcs.breakCurve](SketchArcs_breakCurve_Sample.htm) | Demonstrates the SketchArc.breakCurve method. |
| [SketchArcs.extend](SketchArcs_extend_Sample.htm) | Demonstrates the SketchArc.extend method. |
| [SketchArcs.split](SketchArcs_split_Sample.htm) | Demonstrates the SketchArc.split method. |
| [SketchArcs.trim](SketchArcs_trim_Sample.htm) | Demonstrates the SketchArc.trim method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |