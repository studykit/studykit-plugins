# ConfigurationTable.rows Property

Parent Object: [ConfigurationTable](ConfigurationTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTable\_var" is a variable referencing a ConfigurationTable object. |

"configurationTable\_var" is a variable referencing a ConfigurationTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |