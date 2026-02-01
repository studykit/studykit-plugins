# CustomGraphicsShowThroughColorEffect.color Property

Parent Object: [CustomGraphicsShowThroughColorEffect](CustomGraphicsShowThroughColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsShowThroughColorEffect.h>

## Description

Gets and sets the color associated with this CustomGraphicsShowThroughColorEffect object. The color that will be used to render the portion of the entity that is covered by other objects in the scene.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsShowThroughColorEffect\_var" is a variable referencing a CustomGraphicsShowThroughColorEffect object. |

"customGraphicsShowThroughColorEffect\_var" is a variable referencing a CustomGraphicsShowThroughColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsShowThroughColorEffect.h>  // Get the value of the property. Ptr<Color> propertyValue = customGraphicsShowThroughColorEffect_var->color();  // Set the value of the property, where value_var is a Color. bool returnValue = customGraphicsShowThroughColorEffect_var->color(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |