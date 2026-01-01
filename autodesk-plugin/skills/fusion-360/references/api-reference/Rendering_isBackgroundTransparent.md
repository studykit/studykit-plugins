# Rendering.isBackgroundTransparent Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Specifies if the background of the rendering should be transparent. The default is false, which means it will not be transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. boolean propertyValue = rendering_var->isBackgroundTransparent();  // Set the value of the property, where value_var is a boolean. bool returnValue = rendering_var->isBackgroundTransparent(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |