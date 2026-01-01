# SceneSettings.cameraExposure Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets if the exposure of the camera as specified using the "Exposure Value" (EV). Valid values are between -15.0 and 25.0, inclusive.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. double propertyValue = sceneSettings_var->cameraExposure();  // Set the value of the property, where value_var is a double. bool returnValue = sceneSettings_var->cameraExposure(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |