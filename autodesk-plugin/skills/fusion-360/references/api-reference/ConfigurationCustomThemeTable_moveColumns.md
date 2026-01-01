# ConfigurationCustomThemeTable.moveColumns Method

Parent Object: [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationCustomThemeTable.h>

## Description

Moves the specified columns from one table to another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationCustomThemeTable\_var" is a variable referencing a [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) object.```` ``` returnValue = configurationCustomThemeTable_var.moveColumns(columns, targetTable) ``` ```` |

"configurationCustomThemeTable\_var" is a variable referencing a [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationColumn](ConfigurationColumn.htm)[] | Returns an array of the columns created due to the move. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| columns | ConfigurationColumn[] | An array of the columns within this table that you want to move. |
| targetTable | [ConfigurationTable](ConfigurationTable.htm) | The table you want to move the columns to. The target must be either a top table or a custom theme table. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |