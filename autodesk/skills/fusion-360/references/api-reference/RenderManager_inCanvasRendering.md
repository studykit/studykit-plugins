# RenderManager.inCanvasRendering Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Provides access to the in-canvas rendering capabilities of Fusion. This uses the active viewport and the user will see the rendering as it takes place.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object. |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. Ptr<InCanvasRendering> propertyValue = renderManager_var->inCanvasRendering(); ``` ```` |

## Property Value

This is a read only property whose value is an [InCanvasRendering](InCanvasRendering.htm).

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |