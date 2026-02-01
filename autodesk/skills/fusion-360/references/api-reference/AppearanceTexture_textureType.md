# AppearanceTexture.textureType Property

Parent Object: [AppearanceTexture](AppearanceTexture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTexture.h>

## Description

Gets the type of texture this appearance currently is.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. |

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. ```` ``` #include <Core/Materials/AppearanceTexture.h>  // Get the value of the property. TextureTypes propertyValue = appearanceTexture_var->textureType(); ``` ```` |

## Property Value

This is a read only property whose value is a [TextureTypes](TextureTypes.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |