# ColorProperty.hasConnectedTexture Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Specifies if this color is specified using a simple color or a texture. If this returns true the color is defined using a texture. If the parent is writable, this property can be set to true to change the definition from a simple color to a texture. You can then use the ConnectedTexture property to get the associated texture and modify it.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. boolean propertyValue = colorProperty_var->hasConnectedTexture();  // Set the value of the property, where value_var is a boolean. bool returnValue = colorProperty_var->hasConnectedTexture(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |