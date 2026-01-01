# CustomGraphicsAppearanceColorEffect.appearance Property

Parent Object: [CustomGraphicsAppearanceColorEffect](CustomGraphicsAppearanceColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsAppearanceColorEffect.h>

## Description

Gets and sets the appearance to use. The appearance assigned must be available in the design where the graphics will be drawn.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsAppearanceColorEffect\_var" is a variable referencing a CustomGraphicsAppearanceColorEffect object. |

"customGraphicsAppearanceColorEffect\_var" is a variable referencing a CustomGraphicsAppearanceColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsAppearanceColorEffect.h>  // Get the value of the property. Ptr<Appearance> propertyValue = customGraphicsAppearanceColorEffect_var->appearance();  // Set the value of the property, where value_var is an Appearance. bool returnValue = customGraphicsAppearanceColorEffect_var->appearance(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [Appearance](Appearance.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |