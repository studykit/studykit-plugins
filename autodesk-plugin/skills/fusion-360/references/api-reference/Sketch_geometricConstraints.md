# Sketch.geometricConstraints Property

Parent Object: [Sketch](Sketch.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Sketch.h>

## Description

Returns the sketch constraints collection associated with this sketch. This provides access to the existing sketch constraints and supports the creation of new sketch constraints.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketch\_var" is a variable referencing a Sketch object. |

"sketch\_var" is a variable referencing a Sketch object. ```` ``` #include <Fusion/Sketch/Sketch.h>  // Get the value of the property. Ptr<GeometricConstraints> propertyValue = sketch_var->geometricConstraints(); ``` ```` |

## Property Value

This is a read only property whose value is a [GeometricConstraints](GeometricConstraints.htm).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [GeometricConstraint.addHorizontal](GeometricConstraint_addHorizontal_Sample.htm) | Demonstrates the GeometricConstraint.addHorizontal method. |
| [GeometricConstraint.addHorizontalPoints](GeometricConstraint_addHorizontalPoints_Sample.htm) | Demonstrates the GeometricConstraint.addHorizontalPoints method. |
| [GeometricConstraint.addMidPont](GeometricConstraint_addMidPont_Sample.htm) | Demonstrate the GeometricConstraint.addMidPont method. |
| [GeometricConstraints.addCoincident](GeometricConstraints_addCoincident_Sample.htm) | Demonstrates the GeometricConstraints.addCoincident method. |
| [GeometricConstraints.addCollinear](GeometricConstraints_addCollinear_Sample.htm) | Demonstrates the GeometricConstraints.addCollinear method. |
| [GeometricConstraints.addConcentric](GeometricConstraints_addConcentric_Sample.htm) | Demonstrates the GeometricConstraints.addConcentric method. |
| [GeometricConstraints.addEqual](GeometricConstraints_addEqual_Sample.htm) | Demonstrates the GeometricConstraints.addEqual method. |
| [GeometricConstraints.addParallel](GeometricConstraints_addParallel_Sample.htm) | Demonstrate the GeometricConstraints.addParallel method. |
| [GeometricConstraints.addPerpendicular](GeometricConstraints_addPerpendicular_Sample.htm) | Demonstrates the GeometricConstraints.addPerpendicular method. |
| [GeometricConstraints.addSmooth](GeometricConstraints_addSmooth_Sample.htm) | Demonstrate the GeometricConstraints.addSmooth method. |
| [GeometricConstraints.addSymmetry](GeometricConstraints_addSymmetry_Sample.htm) | Demonstrates the GeometricConstraints.addSymmetry method. |
| [GeometricConstraints.addTangent](GeometricConstraints_addTangent_Sample.htm) | Demonstrates the GeometricConstraints.addTangent method. |
| [GeometricConstraints.addVertical](GeometricConstraints_addVertical_Sample.htm) | Demonstrates the GeometricConstraints.addVertical method. |
| [SketchCircles.addByTwoTangents](SketchCircles_addByTwoTangents_Sample.htm) | Demonstrates the SketchCircles.addByTwoTangets method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |