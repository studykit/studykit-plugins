# InCanvasRendering.isAdvanced Property

Parent Object: [InCanvasRendering](InCanvasRendering.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/InCanvasRendering.h>

## Description

Gets and sets if "Fast" or "Advanced" rendering should be used. If false, "Fast" rendering is used, which uses simplified lighting and materials.

## Syntax

* [Python](#Python)
* [C++](#C++)

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object.  ```` ``` # Get the value of the property. propertyValue = inCanvasRendering_var.isAdvanced  # Set the value of the property. inCanvasRendering_var.isAdvanced = propertyValue ``` ```` |

"inCanvasRendering\_var" is a variable referencing an InCanvasRendering object. ```` ``` #include <Fusion/Render/InCanvasRendering.h>  // Get the value of the property. boolean propertyValue = inCanvasRendering_var->isAdvanced();  // Set the value of the property, where value_var is a boolean. bool returnValue = inCanvasRendering_var->isAdvanced(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version September 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |