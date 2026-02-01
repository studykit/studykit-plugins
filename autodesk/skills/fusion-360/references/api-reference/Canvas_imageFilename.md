# Canvas.imageFilename Property

Parent Object: [Canvas](Canvas.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Image/Canvas.h>

## Description

Gets and sets the filename of the image used for the canvas. When getting this property, the filename returned is the file that was used when the canvas was initially created. it's possible the file may no longer exist.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvas\_var" is a variable referencing a Canvas object.  ```` ``` # Get the value of the property. propertyValue = canvas_var.imageFilename  # Set the value of the property. canvas_var.imageFilename = propertyValue ``` ```` |

"canvas\_var" is a variable referencing a Canvas object. ```` ``` #include <Fusion/Image/Canvas.h>  // Get the value of the property. string propertyValue = canvas_var->imageFilename();  // Set the value of the property, where value_var is a string. bool returnValue = canvas_var->imageFilename(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |