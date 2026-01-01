# ConfigurationPlasticRuleColumns.add Method

Parent Object: [ConfigurationPlasticRuleColumns](ConfigurationPlasticRuleColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleColumns.h>

## Description

Adds a new column to the plastic rule table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleColumns\_var" is a variable referencing a [ConfigurationPlasticRuleColumns](ConfigurationPlasticRuleColumns.htm) object.```` ``` returnValue = configurationPlasticRuleColumns_var.add(component) ``` ```` |

"configurationPlasticRuleColumns\_var" is a variable referencing a [ConfigurationPlasticRuleColumns](ConfigurationPlasticRuleColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm) | Returns the newly created ConfigurationPlasticRuleColumn object or null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| component | [Component](Component.htm) | The component whose active plastic rule will be controlled by this column. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |