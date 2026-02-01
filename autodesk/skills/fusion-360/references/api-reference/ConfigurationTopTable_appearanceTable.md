# ConfigurationTopTable.appearanceTable Property

Parent Object: [ConfigurationTopTable](ConfigurationTopTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTopTable.h>

## Description

Returns the appearance table associated with this top table. The returned table can be empty and not have any columns. In this case, the table is not displayed in the user interface. Use the returned table to add columns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. |

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTopTable.h>  // Get the value of the property. Ptr<ConfigurationAppearanceTable> propertyValue = configurationTopTable_var->appearanceTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |