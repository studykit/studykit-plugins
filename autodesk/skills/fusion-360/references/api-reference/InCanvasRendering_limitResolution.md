# InCanvasRendering.limitResolution Property

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

Sets the percentage of the full resolution to render the image. Valid values are between 20 and 100 inclusive. 100 is full resolution (100%).

## Syntax

* [Python](#Python)
* [C++](#C++)

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object. |

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object. ```` ``` #include <Fusion/Render/InCanvasRendering.h>  // Get the value of the property. double propertyValue = inCanvasRendering_var->limitResolution();  // Set the value of the property, where value_var is a double. bool returnValue = inCanvasRendering_var->limitResolution(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |