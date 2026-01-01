# ConfigurationRow.parentTable Property

Parent Object: [ConfigurationRow](ConfigurationRow.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationRow.h>

## Description

Returns the configuration table this row is a member of.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationRow\_var" is a variable referencing a ConfigurationRow object. |

"configurationRow\_var" is a variable referencing a ConfigurationRow object. ```` ``` #include <Fusion/Configurations/ConfigurationRow.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationRow_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |