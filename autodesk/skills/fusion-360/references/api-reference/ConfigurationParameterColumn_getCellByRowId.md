# ConfigurationParameterColumn.getCellByRowId Method

Parent Object: [ConfigurationParameterColumn](ConfigurationParameterColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationParameterColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationParameterColumn\_var" is a variable referencing a [ConfigurationParameterColumn](ConfigurationParameterColumn.htm) object.```` ``` returnValue = configurationParameterColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationParameterColumn\_var" is a variable referencing a [ConfigurationParameterColumn](ConfigurationParameterColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationParameterCell](ConfigurationParameterCell.htm) | Returns the specified cell if successful and null if the id is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowId | string | The ID of the row to return the cell for. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |