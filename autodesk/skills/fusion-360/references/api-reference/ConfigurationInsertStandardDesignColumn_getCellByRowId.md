# ConfigurationInsertStandardDesignColumn.getCellByRowId Method

Parent Object: [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationInsertStandardDesignColumn.h>

## Description

Gets the cell in this column at the row specified by its ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationInsertStandardDesignColumn\_var" is a variable referencing a [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm) object.```` ``` returnValue = configurationInsertStandardDesignColumn_var.getCellByRowId(rowId) ``` ```` |

"configurationInsertStandardDesignColumn\_var" is a variable referencing a [ConfigurationInsertStandardDesignColumn](ConfigurationInsertStandardDesignColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationInsertStandardDesignCell](ConfigurationInsertStandardDesignCell.htm) | Returns the specified cell if successful and null if the id is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowId | string | The ID of the row to return the cell for. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |