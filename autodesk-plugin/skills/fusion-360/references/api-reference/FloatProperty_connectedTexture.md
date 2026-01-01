# FloatProperty.connectedTexture Property

Parent Object: [FloatProperty](FloatProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/FloatProperty.h>

## Description

When the property is associated with an appearance, this gets the associated texture, if one exists. The HasConnectedTexture property controls if there is an associated texture or not. If it's parent writable you can edit the texture. If no texture exists, this property will return null.

## Syntax

* [Python](#Python)
* [C++](#C++)

"floatProperty\_var" is a variable referencing a FloatProperty object. |

"floatProperty\_var" is a variable referencing a FloatProperty object. ```` ``` #include <Core/Application/FloatProperty.h>  // Get the value of the property. Ptr<AppearanceTexture> propertyValue = floatProperty_var->connectedTexture(); ``` ```` |

## Property Value

This is a read only property whose value is an [AppearanceTexture](AppearanceTexture.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |