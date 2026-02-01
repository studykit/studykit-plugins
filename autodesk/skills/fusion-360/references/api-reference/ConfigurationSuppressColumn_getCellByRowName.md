# ConfigurationSuppressColumn.getCellByRowName Method

Parent Object: [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationSuppressColumn.h>

## Description

Gets the cell in this column at the row specified by its name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationSuppressColumn\_var" is a variable referencing a [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm) object.```` ``` returnValue = configurationSuppressColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationSuppressColumn\_var" is a variable referencing a [ConfigurationSuppressColumn](ConfigurationSuppressColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationSuppressCell](ConfigurationSuppressCell.htm) | Returns the specified cell if successful and null if the name is not found. |

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