# ConfigurationPropertyCell.value Property

Parent Object: [ConfigurationPropertyCell](ConfigurationPropertyCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyCell.h>

## Description

Gets and sets the value of the property associated with the parent column of this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. |

"configurationPropertyCell\_var" is a variable referencing a ConfigurationPropertyCell object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyCell.h>  // Get the value of the property. string propertyValue = configurationPropertyCell_var->value();  // Set the value of the property, where value_var is a string. bool returnValue = configurationPropertyCell_var->value(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |