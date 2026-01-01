# SceneSettings.aspectRatio Property

Parent Object: [SceneSettings](SceneSettings.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/SceneSettings.h>

## Description

Gets and sets the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. To define a custom aspect ratio set this property to CustomRenderAspectRatio and use the aspectRatioHeight and aspectRatioWidth properties to define any aspect ratio.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sceneSettings\_var" is a variable referencing a SceneSettings object.  ```` ``` # Get the value of the property. propertyValue = sceneSettings_var.aspectRatio  # Set the value of the property. sceneSettings_var.aspectRatio = propertyValue ``` ```` |

"sceneSettings\_var" is a variable referencing a SceneSettings object. ```` ``` #include <Fusion/Render/SceneSettings.h>  // Get the value of the property. RenderAspectRatios propertyValue = sceneSettings_var->aspectRatio();  // Set the value of the property, where value_var is a RenderAspectRatios. bool returnValue = sceneSettings_var->aspectRatio(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RenderAspectRatios](RenderAspectRatios.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |