# GraphicsPreferences.isWoodBumpEnabled Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

Gets and sets whether the bump effect is enabled when supported by the Wood (Solid) and the graphics driver. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object.  ```` ``` # Get the value of the property. propertyValue = graphicsPreferences_var.isWoodBumpEnabled  # Set the value of the property. graphicsPreferences_var.isWoodBumpEnabled = propertyValue ``` ```` |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. boolean propertyValue = graphicsPreferences_var->isWoodBumpEnabled();  // Set the value of the property, where value_var is a boolean. bool returnValue = graphicsPreferences_var->isWoodBumpEnabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |