# CustomGraphicsSolidColorEffect.color Property

Parent Object: [CustomGraphicsSolidColorEffect](CustomGraphicsSolidColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>

## Description

The color to use for the solid color display. The opacity component of the color is ignored because the opacity of custom graphics is controlled separately using an opacity attribute.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsSolidColorEffect\_var" is a variable referencing a CustomGraphicsSolidColorEffect object. |

"customGraphicsSolidColorEffect\_var" is a variable referencing a CustomGraphicsSolidColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsSolidColorEffect.h>  // Get the value of the property. Ptr<Color> propertyValue = customGraphicsSolidColorEffect_var->color();  // Set the value of the property, where value_var is a Color. bool returnValue = customGraphicsSolidColorEffect_var->color(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |