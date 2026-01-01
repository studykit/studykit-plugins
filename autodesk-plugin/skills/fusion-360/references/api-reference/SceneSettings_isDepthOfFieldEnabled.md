# SceneSettings.isDepthOfFieldEnabled Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets if the depth of field option is enabled. When setting this to true, use the centerOfFocus and depthOfFieldBlur properties to specify how the depth of field is defined.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object. |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. boolean propertyValue = sceneSettings_var->isDepthOfFieldEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = sceneSettings_var->isDepthOfFieldEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |