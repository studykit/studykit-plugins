# SceneSettings.groundOffset Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the distance of the ground from the bottom of the model. A value of 0 is at the bottom of the model and a positive value moves the plane up and negative down. The value is in centimeters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.groundOffset  # Set the value of the property. sceneSettings_var.groundOffset = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. double propertyValue = sceneSettings_var->groundOffset();  // Set the value of the property, where value_var is a double. bool returnValue = sceneSettings_var->groundOffset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |