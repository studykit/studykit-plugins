# Rendering.aspectRatio Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Gets and sets the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. To define a custom aspect ratio set this property to CustomAspectRatio and use the resolutionHeight and resolutionWidth properties to define the resolution and aspect ratio. The default value is the aspect ratio defined in the scene settings. The width and height must be between 108 and 4000 pixels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. RenderAspectRatios propertyValue = rendering_var->aspectRatio();  // Set the value of the property, where value_var is a RenderAspectRatios. bool returnValue = rendering_var->aspectRatio(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [RenderAspectRatios](RenderAspectRatios.htm).

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |