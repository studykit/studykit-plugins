# ConfigurationMaterialTable.rows Property

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. |

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationMaterialTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |