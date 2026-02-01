# CanvasEffects.isGroundReflectionEnabled Property

Parent Object: [CanvasEffects](CanvasEffects.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/CanvasEffects.h>

## Description

Gets and sets if ground reflection is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"canvasEffects\_var" is a variable referencing a CanvasEffects object.  ```` ``` # Get the value of the property. propertyValue = canvasEffects_var.isGroundReflectionEnabled  # Set the value of the property. canvasEffects_var.isGroundReflectionEnabled = propertyValue ``` ```` |

"canvasEffects\_var" is a variable referencing a CanvasEffects object. ```` ``` #include <Core/Application/CanvasEffects.h>  // Get the value of the property. boolean propertyValue = canvasEffects_var->isGroundReflectionEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = canvasEffects_var->isGroundReflectionEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |