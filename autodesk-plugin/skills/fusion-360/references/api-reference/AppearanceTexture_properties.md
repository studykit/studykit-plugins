# AppearanceTexture.properties Property

Parent Object: [AppearanceTexture](AppearanceTexture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTexture.h>

## Description

Returns a collection of the properties associated with this texture.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. |

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. ```` ``` #include <Core/Materials/AppearanceTexture.h>  // Get the value of the property. Ptr<Properties> propertyValue = appearanceTexture_var->properties(); ``` ```` |

## Property Value

This is a read only property whose value is a [Properties](Properties.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |