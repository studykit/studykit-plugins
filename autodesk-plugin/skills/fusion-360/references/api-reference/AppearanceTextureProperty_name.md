# AppearanceTextureProperty.name Property

Parent Object: [AppearanceTextureProperty](AppearanceTextureProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Materials/AppearanceTextureProperty.h>

## Description

Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

## Syntax

* [Python](#Python)
* [C++](#C++)

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. |

"appearanceTextureProperty\_var" is a variable referencing an AppearanceTextureProperty object. ```` ``` #include <Core/Materials/AppearanceTextureProperty.h>  // Get the value of the property. string propertyValue = appearanceTextureProperty_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |