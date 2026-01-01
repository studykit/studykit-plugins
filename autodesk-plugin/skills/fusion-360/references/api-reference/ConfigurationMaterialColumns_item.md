# ConfigurationMaterialColumns.item Method

Parent Object: [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumns.h>

## Description

A method that returns the specified column using an index into the collection. These are returned in the same order as they appear in the table.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object.```` ``` returnValue = configurationMaterialColumns_var.item(index) ``` ```` |

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) | Returns the specified column or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | uinteger | The index of the column to return, where the first column is index 0. The name column is not included. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |