# Rendering.renderQuality Property

Parent Object: [Rendering](Rendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/Rendering.h>

## Description

Gets and sets the desired quality of the rendering. The quality is specified using a value between 25 and 100, where 75 is the equivalent of "Final" and 100 is the same as "Excellent" in the user interface. The default value is 75

## Syntax

* [Python](#Python)
* [C++](#C++)

"rendering\_var" is a variable referencing a Rendering object. |

"rendering\_var" is a variable referencing a Rendering object. ```` ``` #include <Fusion/Render/Rendering.h>  // Get the value of the property. integer propertyValue = rendering_var->renderQuality();  // Set the value of the property, where value_var is an integer. bool returnValue = rendering_var->renderQuality(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |