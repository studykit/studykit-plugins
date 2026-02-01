# ConfigurationPlasticRuleColumn.getCellByRowName Method

Parent Object: [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleColumn.h>

## Description

Gets the cell in this column at the row specified by its name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleColumn\_var" is a variable referencing a [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm) object.```` ``` returnValue = configurationPlasticRuleColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationPlasticRuleColumn\_var" is a variable referencing a [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationPlasticRuleCell](ConfigurationPlasticRuleCell.htm) | Returns the specified cell if successful and null if the name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowName | string | The name of the row to return the cell for. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |