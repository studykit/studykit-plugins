# StringProperty.value Property

Parent Object: [StringProperty](StringProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StringProperty.h>

## Description

Gets and sets the property value.

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringProperty\_var" is a variable referencing a StringProperty object. |

"stringProperty\_var" is a variable referencing a StringProperty object. ```` ``` #include <Core/Application/StringProperty.h>  // Get the value of the property. string propertyValue = stringProperty_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = stringProperty_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |