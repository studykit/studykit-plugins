# AppearanceTextureProperty.isUsed Property

Parent Object: [AppearanceTextureProperty](AppearanceTextureProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTextureProperty.h>

## Description

Specifies if this AppearanceTexture is being used. This is the equivalent of the check box in the Appearance dialog to enable the use of a text for an appearance or not. if this is False, then the value property should not be used because there isn't an associated. AppearanceTexture.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. |

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. ```` ``` #include <Core/Materials/AppearanceTextureProperty.h>  // Get the value of the property. boolean propertyValue = appearanceTextureProperty_var->isUsed(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |