# ConfigurationInsertCell.row Property

Parent Object: [ConfigurationInsertCell](ConfigurationInsertCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertCell.h>

## Description

Gets and sets which row of the configured design is used for this cell. When setting this property, the row must come from the configured design used by the occurrence associated with the parent column of this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object. |

"configurationInsertCell\_var" is a variable referencing a ConfigurationInsertCell object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationInsertCell_var->row();  // Set the value of the property, where value_var is a ConfigurationRow. bool returnValue = configurationInsertCell_var->row(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |