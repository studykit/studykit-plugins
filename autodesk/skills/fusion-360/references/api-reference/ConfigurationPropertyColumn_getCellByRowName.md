# ConfigurationPropertyColumn.getCellByRowName Method

Parent Object: [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationPropertyColumn.h>

## Description

Gets the cell in this column at the row specified by its name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationPropertyColumn\_var" is a variable referencing a [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm) object.```` ``` returnValue = configurationPropertyColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationPropertyColumn\_var" is a variable referencing a [ConfigurationPropertyColumn](ConfigurationPropertyColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationPropertyCell](ConfigurationPropertyCell.htm) | Returns the specified cell if successful and null if the name is not found. |

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