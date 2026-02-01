# ConfigurationAppearanceColumns.itemById Method

Parent Object: [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumns.h>

## Description

A method that returns the column with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumns\_var" is a variable referencing a [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm) object.```` ``` returnValue = configurationAppearanceColumns_var.itemById(id) ``` ```` |

"configurationAppearanceColumns\_var" is a variable referencing a [ConfigurationAppearanceColumns](ConfigurationAppearanceColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm) | Returns the specified column or null if a column with the specified ID does not exist. |

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