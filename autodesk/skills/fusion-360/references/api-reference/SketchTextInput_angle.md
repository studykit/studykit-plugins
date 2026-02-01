# SketchTextInput.angle Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This property was retired when Fusion added support for sketch along a curve, where defining a rotation angle doesn't make sense. When creating multi-line text you can use the Sketch.move command to rotate and/or move the four lines defining the bounding rectangle of the text.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object.  ```` ``` # Get the value of the property. propertyValue = sketchTextInput_var.angle  # Set the value of the property. sketchTextInput_var.angle = propertyValue ``` ```` |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. double propertyValue = sketchTextInput_var->angle();  // Set the value of the property, where value_var is a double. bool returnValue = sketchTextInput_var->angle(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version March 2015
Retired in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |