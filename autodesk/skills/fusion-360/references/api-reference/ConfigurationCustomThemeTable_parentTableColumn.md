# ConfigurationCustomThemeTable.parentTableColumn Property

Parent Object: [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTable.h>

## Description

Returns the column in the top table that references this custom theme table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. |

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. ```` ``` #include <Fusion/Configurations/ConfigurationCustomThemeTable.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationCustomThemeTable_var->parentTableColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |