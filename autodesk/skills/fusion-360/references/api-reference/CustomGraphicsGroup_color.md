# CustomGraphicsGroup.color Property

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Gets and sets the current color definition for this entity. The color of custom graphics can be defined in many ways; solid color, simple material, and appearance.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. |

"customGraphicsGroup\_var" is a variable referencing a CustomGraphicsGroup object. ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  // Get the value of the property. Ptr<CustomGraphicsColorEffect> propertyValue = customGraphicsGroup_var->color();  // Set the value of the property, where value_var is a CustomGraphicsColorEffect. bool returnValue = customGraphicsGroup_var->color(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [CustomGraphicsColorEffect](CustomGraphicsColorEffect.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |