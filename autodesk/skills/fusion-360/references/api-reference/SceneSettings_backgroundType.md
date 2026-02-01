# SceneSettings.backgroundType Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Specifies the current type of background being used to render the scene. To change the background type use either the backgroundEnvironment or the backgroundSolidColor to set the environment or color.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. RenderSceneBackgroundTypes propertyValue = sceneSettings_var->backgroundType(); ``` ```` |

## Property Value

This is a read only property whose value is a [RenderSceneBackgroundTypes](RenderSceneBackgroundTypes.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |