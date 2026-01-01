# RenderManager.isValid Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object. |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. boolean propertyValue = renderManager_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |