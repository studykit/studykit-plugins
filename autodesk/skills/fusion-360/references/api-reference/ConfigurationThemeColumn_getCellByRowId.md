# ConfigurationThemeColumn.getCellByRowId Method

Parent Object: [ConfigurationThemeColumn](ConfigurationThemeColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationThemeColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationThemeColumn\_var" is a variable referencing a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm) object.```` ``` returnValue = configurationThemeColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationThemeColumn\_var" is a variable referencing a [ConfigurationThemeColumn](ConfigurationThemeColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationThemeCell](ConfigurationThemeCell.htm) | Returns the specified cell if successful and null if the id is not found. |

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