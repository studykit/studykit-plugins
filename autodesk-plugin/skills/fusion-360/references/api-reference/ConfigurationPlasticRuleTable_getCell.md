# ConfigurationPlasticRuleTable.getCell Method

Parent Object: [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleTable.h>

## Description

Returns the cell at the specified row and column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleTable\_var" is a variable referencing a [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm) object.```` ``` returnValue = configurationPlasticRuleTable_var.getCell(column, row) ``` ```` |

"configurationPlasticRuleTable\_var" is a variable referencing a [ConfigurationPlasticRuleTable](ConfigurationPlasticRuleTable.htm) object. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| column | uinteger | The index of the column the cell is in. An index of 0 is the first column and does not include the name column. |
| row | uinteger | The index of the row the cell is in. An index of 0 is the first row and does not include the header row. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |