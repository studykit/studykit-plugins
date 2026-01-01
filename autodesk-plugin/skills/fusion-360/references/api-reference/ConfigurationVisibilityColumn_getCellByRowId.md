# ConfigurationVisibilityColumn.getCellByRowId Method

Parent Object: [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationVisibilityColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationVisibilityColumn\_var" is a variable referencing a [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm) object.```` ``` returnValue = configurationVisibilityColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationVisibilityColumn\_var" is a variable referencing a [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationVisibilityCell](ConfigurationVisibilityCell.htm) | Returns the specified cell if successful and null if the id is not found. |

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