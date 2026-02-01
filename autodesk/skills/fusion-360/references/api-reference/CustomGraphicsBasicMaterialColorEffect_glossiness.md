# CustomGraphicsBasicMaterialColorEffect.glossiness Property

Parent Object: [CustomGraphicsBasicMaterialColorEffect](CustomGraphicsBasicMaterialColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>

## Description

Gets and sets the glossiness associated with this CustomGraphicsBasicMaterialColorEffect object. The glossiness determines the size of highlights, and thus the apparent shininess of the material. A value of 0.0 will result in very large highlights like you would see with a rough surface. A maximum value of 128.0 will result in very small highlight as from a smooth surface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. |

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>  // Get the value of the property. double propertyValue = customGraphicsBasicMaterialColorEffect_var->glossiness();  // Set the value of the property, where value_var is a double. bool returnValue = customGraphicsBasicMaterialColorEffect_var->glossiness(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a double.

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |