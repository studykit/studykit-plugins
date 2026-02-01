# SceneSettings.backgroundEnvironment Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the environment to use for the background. The available environments can be accessed through the RenderManager.renderEnvironments property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.backgroundEnvironment  # Set the value of the property. sceneSettings_var.backgroundEnvironment = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. Ptr<RenderEnvironment> propertyValue = sceneSettings_var->backgroundEnvironment();  // Set the value of the property, where value_var is a RenderEnvironment. bool returnValue = sceneSettings_var->backgroundEnvironment(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RenderEnvironment](RenderEnvironment.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |