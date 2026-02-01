# ConfigurationPropertyColumn.parentTable Property

Parent Object: [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyColumn.h>

## Description

Returns the parent table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. |

"configurationPropertyColumn\_var" is a variable referencing a ConfigurationPropertyColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationPropertyColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationPropertyColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |