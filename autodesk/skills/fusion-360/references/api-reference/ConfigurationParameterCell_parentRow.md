# ConfigurationParameterCell.parentRow Property

Parent Object: [ConfigurationParameterCell](ConfigurationParameterCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterCell.h>

## Description

Returns the row this cell is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. |

"configurationParameterCell\_var" is a variable referencing a ConfigurationParameterCell object. ```` ``` #include <Fusion/Configurations/ConfigurationParameterCell.h>  // Get the value of the property. Ptr<ConfigurationRow> propertyValue = configurationParameterCell_var->parentRow(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRow](ConfigurationRow.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |