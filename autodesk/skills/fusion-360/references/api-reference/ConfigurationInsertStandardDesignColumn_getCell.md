# ConfigurationInsertStandardDesignColumn.getCell Method

Parent Object: [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>

## Description

Gets the cell in this column at the specified row. The first row has an index of 0 and does not include the header row.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignColumn\_var" is a variable referencing a [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm) object.```` ``` returnValue = configurationInsertStandardDesignColumn_var.getCell(rowIndex) ``` ```` |

"configurationInsertStandardDesignColumn\_var" is a variable referencing a [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm) | Returns the specified cell if successful and null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowIndex | uinteger | The index of the row to return the cell for. The first row has an index of 0. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |