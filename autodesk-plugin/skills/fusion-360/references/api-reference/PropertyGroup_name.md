# PropertyGroup.name Property

Parent Object: [PropertyGroup](PropertyGroup.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/PropertyGroup.h>

## Description

Returns the name of this group as seen in the user interface. This name is localized and can change based on the current language

## Syntax

* [Python](#Python)
* [C++](#C++)

"propertyGroup\_var" is a variable referencing a PropertyGroup object. |

"propertyGroup\_var" is a variable referencing a PropertyGroup object. ```` ``` #include <Core/Application/PropertyGroup.h>  // Get the value of the property. string propertyValue = propertyGroup_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = propertyGroup_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |