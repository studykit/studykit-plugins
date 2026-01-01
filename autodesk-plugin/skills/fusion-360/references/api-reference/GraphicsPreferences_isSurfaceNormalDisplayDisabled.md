# GraphicsPreferences.isSurfaceNormalDisplayDisabled Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

Gets and sets whether the surface normal display is disabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object.  ```` ``` # Get the value of the property. propertyValue = graphicsPreferences_var.isSurfaceNormalDisplayDisabled  # Set the value of the property. graphicsPreferences_var.isSurfaceNormalDisplayDisabled = propertyValue ``` ```` |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. integer propertyValue = graphicsPreferences_var->isSurfaceNormalDisplayDisabled();  // Set the value of the property, where value_var is an integer. bool returnValue = graphicsPreferences_var->isSurfaceNormalDisplayDisabled(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an integer.

## Version

Introduced in version May 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |