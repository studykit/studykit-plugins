# ConfigurationAppearanceTable.parentTableColumn Property

Parent Object: [ConfigurationAppearanceTable](ConfigurationAppearanceTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceTable.h>

## Description

Returns the column in the top table that references this appearance table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. |

"configurationAppearanceTable\_var" is a variable referencing a ConfigurationAppearanceTable object. ```` ``` #include <Fusion/Configurations/ConfigurationAppearanceTable.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationAppearanceTable_var->parentTableColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |