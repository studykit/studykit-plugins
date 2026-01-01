# ConfigurationPlasticRuleColumn.component Property

Parent Object: [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleColumn.h>

## Description

Returns the Component being modified by this column. This property returns null when the table being queried was obtained from a DataFile object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleColumn\_var" is a variable referencing a ConfigurationPlasticRuleColumn object. |

"configurationPlasticRuleColumn\_var" is a variable referencing a ConfigurationPlasticRuleColumn object. ```` ``` #include <Fusion/Configurations/ConfigurationPlasticRuleColumn.h>  // Get the value of the property. Ptr<Component> propertyValue = configurationPlasticRuleColumn_var->component(); ``` ```` |

## Property Value

This is a read only property whose value is a [Component](Component.htm).

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |