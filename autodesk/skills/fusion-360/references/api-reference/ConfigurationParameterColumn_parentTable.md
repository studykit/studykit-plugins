# ConfigurationParameterColumn.parentTable Property

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

Returns the parent table, either top or custom theme table, this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object. |

"configurationParameterColumn\_var" is a variable referencing a ConfigurationParameterColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationParameterColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |