# GraphicsPreferences.isLimitEffectsDuringNavigation Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

This function is retired. See more information in the 'Remarks' section below.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object.  ```` ``` # Get the value of the property. propertyValue = graphicsPreferences_var.isLimitEffectsDuringNavigation  # Set the value of the property. graphicsPreferences_var.isLimitEffectsDuringNavigation = propertyValue ``` ```` |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. boolean propertyValue = graphicsPreferences_var->isLimitEffectsDuringNavigation();  // Set the value of the property, where value_var is a boolean. bool returnValue = graphicsPreferences_var->isLimitEffectsDuringNavigation(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version May 2022
Retired in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |