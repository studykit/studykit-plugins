# ConfigurationVisibilityColumn.parentTable Property

Parent Object: [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

Returns the parent table, either top or custom theme table, this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object. |

"configurationVisibilityColumn\_var" is a variable referencing a ConfigurationVisibilityColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationVisibilityColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationVisibilityColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |