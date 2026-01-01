# ConfigurationColumns.itemById Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

A method that returns the specified column object using the ID of the column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.itemById(id) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationColumn](ConfigurationColumn.htm) | Returns the specified item or null if no column matches the provided ID. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the column within the collection to return. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |