# ConfigurationThemeColumn.parentTable Property

Parent Object: [ConfigurationThemeColumn](ConfigurationThemeColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeColumn.h>

## Description

Returns the parent table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeColumn\_var" is a variable referencing a ConfigurationThemeColumn object. |

"configurationThemeColumn\_var" is a variable referencing a ConfigurationThemeColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationThemeColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationThemeColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |