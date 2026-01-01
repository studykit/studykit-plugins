# AppearanceTextureProperty.value Property

Parent Object: [AppearanceTextureProperty](AppearanceTextureProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTextureProperty.h>

## Description

Gets and sets this property value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. |

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. ```` ``` #include <Core/Materials/AppearanceTextureProperty.h>  // Get the value of the property. Ptr<AppearanceTexture> propertyValue = appearanceTextureProperty_var->value();  // Set the value of the property, where value_var is an AppearanceTexture. bool returnValue = appearanceTextureProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an [AppearanceTexture](AppearanceTexture.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |