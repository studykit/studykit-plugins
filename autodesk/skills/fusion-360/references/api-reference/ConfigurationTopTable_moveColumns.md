# ConfigurationTopTable.moveColumns Method

Parent Object: [ConfigurationTopTable](ConfigurationTopTable.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationTopTable.h>

## Description

Moves the specified columns from one table to another.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationTopTable\_var" is a variable referencing a [ConfigurationTopTable](ConfigurationTopTable.htm) object.```` ``` returnValue = configurationTopTable_var.moveColumns(columns, targetTable) ``` ```` |

"configurationTopTable\_var" is a variable referencing a [ConfigurationTopTable](ConfigurationTopTable.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationColumn](ConfigurationColumn.htm)[] | Returns an array of the columns created due to the move. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| columns | ConfigurationColumn[] | An array of the columns within the top table you want to move. |
| targetTable | [ConfigurationCustomThemeTable](ConfigurationCustomThemeTable.htm) | The table you want to move the columns to. The target must be a custom theme table. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |