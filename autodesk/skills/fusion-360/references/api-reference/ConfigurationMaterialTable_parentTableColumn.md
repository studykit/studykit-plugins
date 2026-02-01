# ConfigurationMaterialTable.parentTableColumn Property

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Returns the column in the top table that references this material table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. |

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialTable.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationMaterialTable_var->parentTableColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |