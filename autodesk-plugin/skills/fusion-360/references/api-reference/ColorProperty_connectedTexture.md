# ColorProperty.connectedTexture Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Used for appearances and gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If the parent is writable you can edit the texture. If no texture exists, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. Ptr<AppearanceTexture> propertyValue = colorProperty_var->connectedTexture(); ``` ```` |

## Property Value

This is a read only property whose value is an [AppearanceTexture](AppearanceTexture.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |