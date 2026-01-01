# RenderEventArgs.viewport Property

Parent Object: [RenderEventArgs](RenderEventArgs.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEventArgs.h>

## Description

Returns the viewport that the rendering was performed in when the render is an in-canvas rendering.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. |

"renderEventArgs\_var" is a variable referencing a RenderEventArgs object. ```` ``` #include <Fusion/Render/RenderEventArgs.h>  // Get the value of the property. Ptr<Viewport> propertyValue = renderEventArgs_var->viewport(); ``` ```` |

## Property Value

This is a read only property whose value is a [Viewport](Viewport.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |