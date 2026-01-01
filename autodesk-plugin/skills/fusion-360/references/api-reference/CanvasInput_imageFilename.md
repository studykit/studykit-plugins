# CanvasInput.imageFilename Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Gets and sets the filename of the image used for the canvas.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object.  ```` ``` # Get the value of the property. propertyValue = canvasInput_var.imageFilename  # Set the value of the property. canvasInput_var.imageFilename = propertyValue ``` ```` |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. string propertyValue = canvasInput_var->imageFilename();  // Set the value of the property, where value_var is a string. bool returnValue = canvasInput_var->imageFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |