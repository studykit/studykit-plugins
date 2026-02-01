# ConfigurationMaterialColumn.parentMaterialTable Property

Parent Object: [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumn.h>

## Description

Returns the parent material table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. |

"configurationMaterialColumn\_var" is a variable referencing a ConfigurationMaterialColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationMaterialColumn.h>  // Get the value of the property. Ptr<ConfigurationMaterialTable> propertyValue = configurationMaterialColumn_var->parentMaterialTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationMaterialTable](ConfigurationMaterialTable.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |