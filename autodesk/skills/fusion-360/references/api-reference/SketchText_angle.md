# SketchText.angle Property

Parent Object: [SketchText](SketchText.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This was retired when Fusion added support for sketch along a curve and multi-line text, which neither supports getting and setting an angle. For multi-line text you can get the rectangle sketch lines that define the boundary of the text and manipulate those to move and rotate the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchText\_var" is a variable referencing a SketchText object.  ```` ``` # Get the value of the property. propertyValue = sketchText_var.angle  # Set the value of the property. sketchText_var.angle = propertyValue ``` ```` |

"sketchText\_var" is a variable referencing a SketchText object. ```` ``` #include <Fusion/Sketch/SketchText.h>  // Get the value of the property. double propertyValue = sketchText_var->angle();  // Set the value of the property, where value_var is a double. bool returnValue = sketchText_var->angle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version March 2015
Retired in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |