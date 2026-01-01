# RenderManager.renderEnvironments Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Provides access to the provided environments and supports specifying a custom environment. This provides access to the same list of environments that you see in the "Environment Library" tab of the "SCENE SETTINGS" dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object. |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. Ptr<RenderEnvironments> propertyValue = renderManager_var->renderEnvironments(); ``` ```` |

## Property Value

This is a read only property whose value is a [RenderEnvironments](RenderEnvironments.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |