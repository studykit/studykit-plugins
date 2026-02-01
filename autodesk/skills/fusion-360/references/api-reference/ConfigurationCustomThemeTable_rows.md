# ConfigurationCustomThemeTable.rows Property

Parent Object: [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. |

"configurationCustomThemeTable\_var" is a variable referencing a ConfigurationCustomThemeTable object. ```` ``` #include <Fusion/Configurations/ConfigurationCustomThemeTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationCustomThemeTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |