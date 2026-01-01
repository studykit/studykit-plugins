# AppearanceTexture.isValid Property

Parent Object: [AppearanceTexture](AppearanceTexture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTexture.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. |

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. ```` ``` #include <Core/Materials/AppearanceTexture.h>  // Get the value of the property. boolean propertyValue = appearanceTexture_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |