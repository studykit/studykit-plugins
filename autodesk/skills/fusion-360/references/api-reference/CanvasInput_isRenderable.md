# CanvasInput.isRenderable Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Controls if the canvas will be rendered when ray tracing within the Render workspace.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object.  ```` ``` # Get the value of the property. propertyValue = canvasInput_var.isRenderable  # Set the value of the property. canvasInput_var.isRenderable = propertyValue ``` ```` |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. boolean propertyValue = canvasInput_var->isRenderable();  // Set the value of the property, where value_var is a boolean. bool returnValue = canvasInput_var->isRenderable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |