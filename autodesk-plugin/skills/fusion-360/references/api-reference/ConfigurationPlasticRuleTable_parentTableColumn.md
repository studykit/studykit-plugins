# ConfigurationPlasticRuleTable.parentTableColumn Property

Parent Object: [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleTable.h>

## Description

Returns the column in the top table that references this plastic rule table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleTable\_var" is a variable referencing a ConfigurationPlasticRuleTable object. |

"configurationPlasticRuleTable\_var" is a variable referencing a ConfigurationPlasticRuleTable object. ```` ``` #include <Fusion/Configurations/ConfigurationPlasticRuleTable.h>  // Get the value of the property. Ptr<ConfigurationThemeColumn> propertyValue = configurationPlasticRuleTable_var->parentTableColumn(); ``` ```` |

## Property Value

This is a read only property whose value is a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm).

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |