# ConfigurationTopTable.customThemeTables Property

Parent Object: [ConfigurationTopTable](ConfigurationTopTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTopTable.h>

## Description

Returns any custom theme tables associated with this top table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. |

"configurationTopTable\_var" is a variable referencing a ConfigurationTopTable object. ```` ``` #include <Fusion/Configurations/ConfigurationTopTable.h>  // Get the value of the property. Ptr<ConfigurationCustomThemeTables> propertyValue = configurationTopTable_var->customThemeTables(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationCustomThemeTables](ConfigurationCustomThemeTables.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |