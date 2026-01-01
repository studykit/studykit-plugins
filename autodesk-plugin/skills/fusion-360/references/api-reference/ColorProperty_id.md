# ColorProperty.id Property

Parent Object: [ColorProperty](ColorProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/ColorProperty.h>

## Description

Returns the unique ID of this property.

## Syntax

* [Python](#Python)
* [C++](#C++)

"colorProperty\_var" is a variable referencing a ColorProperty object. |

"colorProperty\_var" is a variable referencing a ColorProperty object. ```` ``` #include <Core/Application/ColorProperty.h>  // Get the value of the property. string propertyValue = colorProperty_var->id(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |