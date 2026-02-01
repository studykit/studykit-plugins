# ConfigurationMaterialTable.columns Property

Parent Object: [ConfigurationMaterialTable](ConfigurationMaterialTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialTable.h>

## Description

Returns the collection that provides access to the columns in this table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. |

"configurationMaterialTable\_var" is a variable referencing a ConfigurationMaterialTable object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialTable.h>  // Get the value of the property. Ptr<ConfigurationMaterialColumns> propertyValue = configurationMaterialTable_var->columns(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |