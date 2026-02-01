# ConfigurationMaterialColumns.itemById Method

Parent Object: [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumns.h>

## Description

A method that returns the column with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object.```` ``` returnValue = configurationMaterialColumns_var.itemById(id) ``` ```` |

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) | Returns the specified column or null if a column with the specified ID does not exist. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The id of the column to return. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |