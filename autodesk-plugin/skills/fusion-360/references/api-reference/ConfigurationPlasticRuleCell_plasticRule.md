# ConfigurationPlasticRuleCell.plasticRule Property

Parent Object: [ConfigurationPlasticRuleCell](ConfigurationPlasticRuleCell.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleCell.h>

## Description

Gets and sets the plastic rule defined for this cell.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleCell\_var" is a variable referencing a ConfigurationPlasticRuleCell object. |

"configurationPlasticRuleCell\_var" is a variable referencing a ConfigurationPlasticRuleCell object. ```` ``` #include <Fusion/Configurations/ConfigurationPlasticRuleCell.h>  // Get the value of the property. Ptr<PlasticRule> propertyValue = configurationPlasticRuleCell_var->plasticRule();  // Set the value of the property, where value_var is a PlasticRule. bool returnValue = configurationPlasticRuleCell_var->plasticRule(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [PlasticRule](PlasticRule.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |