# ColorProperty.values Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Gets and sets the values associated with this property. The HasMultipleValues property indicates if this property will be returning more than one value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. std::vector<Ptr<Color>> propertyValue = colorProperty_var->values();  // Set the value of the property, where value_var is a Color. bool returnValue = colorProperty_var->values(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Color](Color.htm).

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |