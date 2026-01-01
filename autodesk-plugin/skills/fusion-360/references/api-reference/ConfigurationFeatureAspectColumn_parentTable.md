# ConfigurationFeatureAspectColumn.parentTable Property

Parent Object: [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>

## Description

This property returns the parent table, either the top or custom theme table this column is in.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectColumn\_var" is a variable referencing a ConfigurationFeatureAspectColumn object. |

"configurationFeatureAspectColumn\_var" is a variable referencing a ConfigurationFeatureAspectColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>  // Get the value of the property. Ptr<ConfigurationTable> propertyValue = configurationFeatureAspectColumn_var->parentTable(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationTable](ConfigurationTable.htm).

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |