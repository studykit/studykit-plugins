# ColorProperty.value Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Gets and sets this property value if there is a color and not a texture defining this color. If a texture is used, this property returns null. Setting this property when a texture is used removes the texture and changes the color definition to a simple color.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. Ptr<Color> propertyValue = colorProperty_var->value();  // Set the value of the property, where value_var is a Color. bool returnValue = colorProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [Color](Color.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |