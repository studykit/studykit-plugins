# SceneSettings.aspectRatioWidth Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the width of the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. For example specifying the width and height of 4:3 is equivalent to setting 20:15. It's only the ratio of the numbers that matters.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.aspectRatioWidth  # Set the value of the property. sceneSettings_var.aspectRatioWidth = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. integer propertyValue = sceneSettings_var->aspectRatioWidth();  // Set the value of the property, where value_var is an integer. bool returnValue = sceneSettings_var->aspectRatioWidth(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |