# SceneSettings.cameraType Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the type of camera to use when rendering the scene.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. CameraTypes propertyValue = sceneSettings_var->cameraType();  // Set the value of the property, where value_var is a CameraTypes. bool returnValue = sceneSettings_var->cameraType(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CameraTypes](CameraTypes.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |