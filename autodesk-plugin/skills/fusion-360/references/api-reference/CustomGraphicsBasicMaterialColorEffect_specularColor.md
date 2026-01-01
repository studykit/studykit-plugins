# CustomGraphicsBasicMaterialColorEffect.specularColor Property

Parent Object: [CustomGraphicsBasicMaterialColorEffect](CustomGraphicsBasicMaterialColorEffect.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>

## Description

Gets and sets the specularColor associated with this CustomGraphicsBasicMaterialColorEffect object. The specular color is the color of reflected light (highlights) as it is reflected off of a shiny surface. This is commonly white or a lighter shade of the emissive color.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. |

"customGraphicsBasicMaterialColorEffect\_var" is a variable referencing a CustomGraphicsBasicMaterialColorEffect object. ```` ``` #include <Fusion/Graphics/CustomGraphicsBasicMaterialColorEffect.h>  // Get the value of the property. Ptr<Color> propertyValue = customGraphicsBasicMaterialColorEffect_var->specularColor();  // Set the value of the property, where value_var is a Color. bool returnValue = customGraphicsBasicMaterialColorEffect_var->specularColor(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |