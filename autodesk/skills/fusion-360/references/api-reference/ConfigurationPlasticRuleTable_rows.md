# ConfigurationPlasticRuleTable.rows Property

Parent Object: [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleTable.h>

## Description

Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleTable\_var" is a variable referencing a ConfigurationPlasticRuleTable object. |

"configurationPlasticRuleTable\_var" is a variable referencing a ConfigurationPlasticRuleTable object. ```` ``` #include <Fusion/Configurations/ConfigurationPlasticRuleTable.h>  // Get the value of the property. Ptr<ConfigurationRows> propertyValue = configurationPlasticRuleTable_var->rows(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationRows](ConfigurationRows.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |