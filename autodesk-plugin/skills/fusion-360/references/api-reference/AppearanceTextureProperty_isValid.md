# AppearanceTextureProperty.isValid Property

Parent Object: [AppearanceTextureProperty](AppearanceTextureProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTextureProperty.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. |

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. ```` ``` #include <Core/Materials/AppearanceTextureProperty.h>  // Get the value of the property. boolean propertyValue = appearanceTextureProperty_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |