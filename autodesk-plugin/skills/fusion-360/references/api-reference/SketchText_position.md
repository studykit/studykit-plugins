# SketchText.position Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property has been retired as a result of Fusion adding support for text along a curve. To move text, you can use the Sketch.move method.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object.  ```` ``` # Get the value of the property. propertyValue = sketchText_var.position  # Set the value of the property. sketchText_var.position = propertyValue ``` ```` |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchText_var->position();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchText_var->position(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version March 2015
Retired in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |