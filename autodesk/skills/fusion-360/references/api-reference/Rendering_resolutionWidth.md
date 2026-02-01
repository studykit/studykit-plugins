# Rendering.resolutionWidth Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Gets and sets the width of the image in pixels. If anything but CustomRenderAspectRatio is defined as the aspect ratio, the resolution height will be modified to maintain the specified aspect ratio. The width must be between 108 and 4000 pixels.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. integer propertyValue = rendering_var->resolutionWidth();  // Set the value of the property, where value_var is an integer. bool returnValue = rendering_var->resolutionWidth(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |