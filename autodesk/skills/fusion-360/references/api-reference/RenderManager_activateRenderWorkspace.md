# RenderManager.activateRenderWorkspace Method

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Activates the Render workspace for this design. If the workspace is already active, nothing happens and it remains active.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a [RenderManager](RenderManager.htm) object.```` ``` returnValue = renderManager_var.activateRenderWorkspace() ``` ```` |

"renderManager\_var" is a variable referencing a [RenderManager](RenderManager.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the activation was succesful or if the Render workspace was already active. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |