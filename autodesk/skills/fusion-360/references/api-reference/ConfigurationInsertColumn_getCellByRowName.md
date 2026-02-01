# ConfigurationInsertColumn.getCellByRowName Method

Parent Object: [ConfigurationInsertColumn](ConfigurationInsertColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertColumn.h>

## Description

Gets the cell in this column at the row specified by its name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertColumn\_var" is a variable referencing a [ConfigurationInsertColumn](ConfigurationInsertColumn.htm) object.```` ``` returnValue = configurationInsertColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationInsertColumn\_var" is a variable referencing a [ConfigurationInsertColumn](ConfigurationInsertColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationInsertCell](ConfigurationInsertCell.htm) | Returns the specified cell if successful and null if the name is not found. |

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