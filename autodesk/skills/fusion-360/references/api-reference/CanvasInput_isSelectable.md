# CanvasInput.isSelectable Property

Parent Object: [CanvasInput](CanvasInput.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/CanvasInput.h>

## Description

Controls if the canvas is selectable or not within the graphics window.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasInput\_var" is a variable referencing a CanvasInput object.  ```` ``` # Get the value of the property. propertyValue = canvasInput_var.isSelectable  # Set the value of the property. canvasInput_var.isSelectable = propertyValue ``` ```` |

"canvasInput\_var" is a variable referencing a CanvasInput object. ```` ``` #include <Fusion/Image/CanvasInput.h>  // Get the value of the property. boolean propertyValue = canvasInput_var->isSelectable();  // Set the value of the property, where value_var is a boolean. bool returnValue = canvasInput_var->isSelectable(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |