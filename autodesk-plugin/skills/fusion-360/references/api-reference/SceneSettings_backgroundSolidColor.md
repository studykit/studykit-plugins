# SceneSettings.backgroundSolidColor Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the background color. When this property is set, it defines the background to be a solid color. The opacity component of the color is ignored.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.backgroundSolidColor  # Set the value of the property. sceneSettings_var.backgroundSolidColor = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. Ptr<Color> propertyValue = sceneSettings_var->backgroundSolidColor();  // Set the value of the property, where value_var is a Color. bool returnValue = sceneSettings_var->backgroundSolidColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |