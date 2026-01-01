# SceneSettings.depthOfFieldBlur Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Specify the amount of blur to apply to objects outside the center of focus. This must be a value between 0.001 and 2.000 inclusive. The depth of field is defined by using the centerOfFocus property to set the depth where the model is in focus.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.depthOfFieldBlur  # Set the value of the property. sceneSettings_var.depthOfFieldBlur = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. double propertyValue = sceneSettings_var->depthOfFieldBlur();  // Set the value of the property, where value_var is a double. bool returnValue = sceneSettings_var->depthOfFieldBlur(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |