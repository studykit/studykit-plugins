# ConfigurationTopTable.columns Property

Parent Object: [ConfigurationTopTable](ConfigurationTopTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTopTable.h>

## Description

Returns the columns defined for this table and provides the functionality to create new columns.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. |

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTopTable.h>  // Get the value of the property. Ptr<ConfigurationColumns> propertyValue = configurationTopTable_var->columns(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationColumns](ConfigurationColumns.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |