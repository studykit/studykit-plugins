# CanvasInput.transform Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Gets and sets the transform of the canvas. This allows you to control the position, rotation, scaling, and flipping. The X and Y axes defined by the matrix, must be perpendicular to one another. The directions of the X and Y axes defines the orientation of the image.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object.  ```` ``` # Get the value of the property. propertyValue = canvasInput_var.transform  # Set the value of the property. canvasInput_var.transform = propertyValue ``` ```` |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. Ptr<Matrix2D> propertyValue = canvasInput_var->transform();  // Set the value of the property, where value_var is a Matrix2D. bool returnValue = canvasInput_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix2D](Matrix2D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |