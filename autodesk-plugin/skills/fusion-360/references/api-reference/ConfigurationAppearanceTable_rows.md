# ConfigurationAppearanceTable.rows Property

Parent Object: [ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. |

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationAppearanceTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |