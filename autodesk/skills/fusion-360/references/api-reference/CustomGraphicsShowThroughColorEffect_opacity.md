# CustomGraphicsShowThroughColorEffect.opacity Property

Parent Object: [CustomGraphicsShowThroughColorEffect](CustomGraphicsShowThroughColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsShowThroughColorEffect.h>

## Description

Gets and sets the opacity value associated with this CustomGraphicsShowThroughColorEffect object. The opacity is used when rendering the portion of the entity that is covered by other objects in the scene. This can be a value between 0 and 1, where 1 is fully opaque and will completely cover any other entities.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsShowThroughColorEffect\_var" is a variable referencing a CustomGraphicsShowThroughColorEffect object. |

"customGraphicsShowThroughColorEffect\_var" is a variable referencing a CustomGraphicsShowThroughColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsShowThroughColorEffect.h>  // Get the value of the property. double propertyValue = customGraphicsShowThroughColorEffect_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsShowThroughColorEffect_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version August 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |