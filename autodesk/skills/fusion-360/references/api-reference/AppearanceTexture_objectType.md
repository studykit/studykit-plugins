# AppearanceTexture.objectType Property

Parent Object: [AppearanceTexture](AppearanceTexture.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTexture.h>

## Description

This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object.  ```` ``` # Get the value of the property. propertyValue = appearanceTexture_var.objectType ``` ```` |

"appearanceTexture\_var" is a variable referencing an AppearanceTexture object. ```` ``` #include <Core/Materials/AppearanceTexture.h>  // Get the value of the property. string propertyValue = appearanceTexture_var->objectType(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |