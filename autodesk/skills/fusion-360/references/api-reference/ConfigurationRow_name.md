# ConfigurationRow.name Property

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Gets and sets the name of this row. Names must be unique with respect to other rows in this table. If you specify a name that exists, Fusion will append a counter to ensure uniqueness. For example, if "Small" is already used and you name another row "Small", you will end up with "Small (1)".

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a ConfigurationRow object. |

"configurationRow\_var" is a variable referencing a ConfigurationRow object. ```` ``` #include <Fusion/Configurations/ConfigurationRow.h>  // Get the value of the property. string propertyValue = configurationRow_var->name();  // Set the value of the property, where value_var is a string. bool returnValue = configurationRow_var->name(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |