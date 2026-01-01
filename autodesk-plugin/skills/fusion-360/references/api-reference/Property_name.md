# Property.name Property

Parent Object: [Property](Property.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Property.h>

## Description

Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

## Syntax

* [Python](#Python)
* [C++](#C++)

"property\_var" is a variable referencing a Property object. |

"property\_var" is a variable referencing a Property object. ```` ``` #include <Core/Application/Property.h>  // Get the value of the property. string propertyValue = property_var->name(); ``` ```` |

## Property Value

This is a read only property whose value is a string.

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |