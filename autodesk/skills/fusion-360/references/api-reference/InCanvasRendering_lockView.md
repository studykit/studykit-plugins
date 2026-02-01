# InCanvasRendering.lockView Property

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

Gets and sets if the view should be locked during the in-canvas render. This prohibits the user from interacting with the view, which will cause the rendering to restart.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object. |

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object. ```` ``` #include <Fusion/Render/InCanvasRendering.h>  // Get the value of the property. boolean propertyValue = inCanvasRendering_var->lockView();  // Set the value of the property, where value_var is a boolean. bool returnValue = inCanvasRendering_var->lockView(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |