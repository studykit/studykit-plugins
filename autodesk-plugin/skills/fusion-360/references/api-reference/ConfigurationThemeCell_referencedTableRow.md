# ConfigurationThemeCell.referencedTableRow Property

Parent Object: [ConfigurationThemeCell](ConfigurationThemeCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeCell.h>

## Description

Gets and sets the row to use from the referenced table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object. |

"configurationThemeCell\_var" is a variable referencing a ConfigurationThemeCell object. ```` ``` #include <Fusion/Configurations/ConfigurationThemeCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationThemeCell_var->referencedTableRow();  // Set the value of the property, where value_var is a ConfigurationRow. bool returnValue = configurationThemeCell_var->referencedTableRow(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |