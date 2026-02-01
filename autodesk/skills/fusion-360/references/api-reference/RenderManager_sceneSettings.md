# RenderManager.sceneSettings Property

Parent Object: [RenderManager](RenderManager.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderManager.h>

## Description

Returns the SceneSettings object that provides access to all of the settings that control how the scene is rendered. This provides equivalent functionality as the "Settings" tab in the "SCENE SETTINGS" dialog.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderManager\_var" is a variable referencing a RenderManager object. |

"renderManager\_var" is a variable referencing a RenderManager object. ```` ``` #include <Fusion/Render/RenderManager.h>  // Get the value of the property. Ptr<SceneSettings> propertyValue = renderManager_var->sceneSettings(); ``` ```` |

## Property Value

This is a read only property whose value is a [SceneSettings](SceneSettings.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |