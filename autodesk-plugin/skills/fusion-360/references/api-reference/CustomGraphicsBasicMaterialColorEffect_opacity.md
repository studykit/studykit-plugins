# CustomGraphicsBasicMaterialColorEffect.opacity Property

Parent Object: [CustomGraphicsBasicMaterialColorEffect](CustomGraphicsBasicMaterialColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>

## Description

Gets and sets the opacity associated with this CustomGraphicsBasicMaterialColorEffect object. A value of 1.0 is completely opaque and 0.0 is completely transparent.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. |

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>  // Get the value of the property. double propertyValue = customGraphicsBasicMaterialColorEffect_var->opacity();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsBasicMaterialColorEffect_var->opacity(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |