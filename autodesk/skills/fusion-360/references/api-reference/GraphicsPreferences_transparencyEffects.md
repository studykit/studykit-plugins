# GraphicsPreferences.transparencyEffects Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

Gets and sets the style of display for transparency effects. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object.  ```` ``` # Get the value of the property. propertyValue = graphicsPreferences_var.transparencyEffects  # Set the value of the property. graphicsPreferences_var.transparencyEffects = propertyValue ``` ```` |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. TransparencyDisplayEffects propertyValue = graphicsPreferences_var->transparencyEffects();  // Set the value of the property, where value_var is a TransparencyDisplayEffects. bool returnValue = graphicsPreferences_var->transparencyEffects(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [TransparencyDisplayEffects](TransparencyDisplayEffects.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |