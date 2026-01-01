# Sketch.sketchPoints Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the sketch points collection associated with this sketch. This provides access to the existing sketch points and supports the creation of new sketch points.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<SketchPoints> propertyValue = sketch_var->sketchPoints(); ``` ```` |

## Property Value

This is a read only property whose value is a [SketchPoints](SketchPoints.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [GeometricConstraint.addMidPont](GeometricConstraint_addMidPont_Sample.htm) | Demonstrate the GeometricConstraint.addMidPont method. |
| [SketchPoint.add](SketchPoint_add_Sample.htm) | Demonstrates the SketchPoint.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |