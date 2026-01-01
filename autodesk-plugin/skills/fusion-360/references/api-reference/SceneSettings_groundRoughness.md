# SceneSettings.groundRoughness Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the roughness of the ground which controls the sharpness of the reflection. This is only used when the isGroundReflections property is true. This is a value between 0 and 1, where 0 is smooth and 1 is rough.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. double propertyValue = sceneSettings_var->groundRoughness();  // Set the value of the property, where value_var is a double. bool returnValue = sceneSettings_var->groundRoughness(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |