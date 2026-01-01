# StringProperty.name Property

Parent Object: [StringProperty](StringProperty.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/StringProperty.h>

## Description

Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

## Syntax

* [Python](#Python)
* [C++](#C++)

"stringProperty\_var" is a variable referencing a StringProperty object. |

"stringProperty\_var" is a variable referencing a StringProperty object. ```` ``` #include <Core/Application/StringProperty.h>  // Get the value of the property. string propertyValue = stringProperty_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |