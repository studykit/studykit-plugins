# SceneSettings.cameraFocalLength Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the focal length of the camera, specified in millimeters. Changing the perspective angle of the camera associated with the active viewport will also change the focal length. Focal length and perspective angle are two different ways to control the same setting.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. double propertyValue = sceneSettings_var->cameraFocalLength();  // Set the value of the property, where value_var is a double. bool returnValue = sceneSettings_var->cameraFocalLength(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |