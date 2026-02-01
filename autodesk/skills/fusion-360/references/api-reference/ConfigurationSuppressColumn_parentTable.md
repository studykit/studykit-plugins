# ConfigurationSuppressColumn.parentTable Property

Parent Object: [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressColumn.h>

## Description

Returns the parent table, either top or custom theme table, this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object. |

"configurationSuppressColumn\_var" is a variable referencing a ConfigurationSuppressColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationSuppressColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationSuppressColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |