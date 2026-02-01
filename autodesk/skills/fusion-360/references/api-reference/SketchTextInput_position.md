# SketchTextInput.position Property

Parent Object: [SketchTextInput](SketchTextInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchTextInput.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Remarks

This method has been retired. The closest equivalent is when creating multi-line text. The setAsMultiLine has a cornerPoint argument that lets you define the position of the text. For text along a curve, the curve defines its positions.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sketchTextInput\_var" is a variable referencing a SketchTextInput object.  ```` ``` # Get the value of the property. propertyValue = sketchTextInput_var.position  # Set the value of the property. sketchTextInput_var.position = propertyValue ``` ```` |

"sketchTextInput\_var" is a variable referencing a SketchTextInput object. ```` ``` #include <Fusion/Sketch/SketchTextInput.h>  // Get the value of the property. Ptr<Point3D> propertyValue = sketchTextInput_var->position();  // Set the value of the property, where value_var is a Point3D. bool returnValue = sketchTextInput_var->position(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Point3D](Point3D.htm).

## Version

Introduced in version March 2015
Retired in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |