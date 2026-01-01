# Point3D.create Method

Parent Object: [Point3D](Point3D.htm)
Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Creates a transient 3D point object.

## Syntax

* [Python](#Python)
* [C++](#C++)

This is a static method. |

This is a static method. ```` ```  #include <Core/Geometry/Point3D.h> ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Point3D](Point3D.htm) | Returns the new Point3D object or null if the creation failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| x | double | The x coordinate of the point   This is an optional argument whose default value is 0.0. |
| y | double | The y coordinate of the point   This is an optional argument whose default value is 0.0. |
| z | double | The z coordinate of the point   This is an optional argument whose default value is 0.0. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Simple Extrusion Sample](SimpleExtrusionSample_Sample.htm) | Creates a new extrusion feature, resulting in a new component. |
| [Simple Revolve Feature Sample](SimpleRevolveFeatureSample_Sample.htm) | Creates a new revolve feature, resulting in a new component. |
| [SketchArcs.addByCenterStartSweep](SketchArcs_addByCenterStartaSweep_Sample.htm) | Demonstrates the SketchArcs.addByCenterStartSweep method. |
| [SketchArcs.addByThreePoints](SketchArcs_addByThreePoints_Sample.htm) | Demonstrates the SketchArcs.addByThreePoints method. |
| [SketchArcs.addFillet](SketchArcs_addFillet_Sample.htm) | Demonstrates the SketchArcs.addFillet method. |
| [SketchArcs.breakCurve](SketchArcs_breakCurve_Sample.htm) | Demonstrates the SketchArc.breakCurve method. |
| [SketchArcs.extend](SketchArcs_extend_Sample.htm) | Demonstrates the SketchArc.extend method. |
| [SketchArcs.trim](SketchArcs_trim_Sample.htm) | Demonstrates the SketchArc.trim method. |
| [SketchCircles.addByCenterRadius](SketchCircles_addByCenterRadius_Sample.htm) | Demonstrates the SketchCircles.addByCenterRadius method. |
| [SketchCircles.addByThreePoints](SketchCircles_addByThreePoints_Sample.htm) | Demonstrates the SketchCircles.addByThreePoints method. |
| [SketchCircles.addByThreeTangents](SketchCircles_addByThreeTangents_Sample.htm) | Demonstrates the SketchCircles.addByThreeTangets method. |
| [SketchCircles.addByTwoPoints](SketchCircles_addByTwoPoints_Sample.htm) | Demonstrates the SketchCircles.addByTwoPoints method. |
| [SketchEllipses.add](SketchEllipses_add_Sample.htm) | Demonstrates the SketchEllipses.add method. |
| [SketchFittedSplines.add](SketchFittedSplines_add_Sample.htm) | Demonstrates the SketchFittedSplines.add method. |
| [SketchLines.addThreePointRectangle](SketchLines_addThreePointRectangle_Sample.htm) | Demonstrates the SketchLines.addThreePointRectangle method. |
| [SketchLines.addTwoPointRectangle](SketchLines_addTwoPointRectangle_Sample.htm) | Demonstrates the SketchLines.addTwoPointRectangle method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |