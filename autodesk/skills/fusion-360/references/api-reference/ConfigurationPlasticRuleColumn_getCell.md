# ConfigurationPlasticRuleColumn.getCell Method

Parent Object: [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPlasticRuleColumn.h>

## Description

Gets the cell in this column at the specified row. The first row has an index of 0 and does not include the header row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPlasticRuleColumn\_var" is a variable referencing a [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm) object.```` ``` returnValue = configurationPlasticRuleColumn_var.getCell(rowIndex) ``` ```` |

"configurationPlasticRuleColumn\_var" is a variable referencing a [ConfigurationPlasticRuleColumn](ConfigurationPlasticRuleColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationPlasticRuleCell](ConfigurationPlasticRuleCell.htm) | Returns the specified cell if successful and null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowIndex | uinteger | The index of the row to return the cell for. The first row has an index of 0. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |