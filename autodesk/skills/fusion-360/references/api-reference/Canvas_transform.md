# Canvas.transform Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Gets and sets the transform of the canvas. This allows you to control the position, rotation, scaling, and flipping. The X and Y axes defined by the matrix and must be perpendicular to one another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object.  ```` ``` # Get the value of the property. propertyValue = canvas_var.transform  # Set the value of the property. canvas_var.transform = propertyValue ``` ```` |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. Ptr<Matrix2D> propertyValue = canvas_var->transform();  // Set the value of the property, where value_var is a Matrix2D. bool returnValue = canvas_var->transform(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Matrix2D](Matrix2D.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |