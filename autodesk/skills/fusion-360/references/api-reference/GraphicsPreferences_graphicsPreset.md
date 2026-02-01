# GraphicsPreferences.graphicsPreset Property

Parent Object: [GraphicsPreferences](GraphicsPreferences.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/GraphicsPreferences.h>

## Description

Gets and sets if the different graphics settings are using predefined settings to get the best performance, quality, or are custom to allow any settings. Setting this to performance or quality will result in other graphics settings changing to match the defined preset.

## Syntax

* [Python](#Python)
* [C++](#C++)

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. |

"graphicsPreferences\_var" is a variable referencing a GraphicsPreferences object. ```` ``` #include <Core/Application/GraphicsPreferences.h>  // Get the value of the property. GraphicsPresets propertyValue = graphicsPreferences_var->graphicsPreset();  // Set the value of the property, where value_var is a GraphicsPresets. bool returnValue = graphicsPreferences_var->graphicsPreset(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [GraphicsPresets](GraphicsPresets.htm).

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |