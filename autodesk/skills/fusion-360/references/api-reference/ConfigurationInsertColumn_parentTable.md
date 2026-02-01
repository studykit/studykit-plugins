# ConfigurationInsertColumn.parentTable Property

Parent Object: [ConfigurationInsertColumn](ConfigurationInsertColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertColumn.h>

## Description

Returns the parent table, either top or custom theme table, this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object. |

"configurationInsertColumn\_var" is a variable referencing a ConfigurationInsertColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationInsertColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationInsertColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |