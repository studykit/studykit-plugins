# ConfigurationAppearanceColumn.getCellByRowName Method

Parent Object: [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationAppearanceColumn.h>

## Description

Gets the cell in this column at the row specified by its name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationAppearanceColumn\_var" is a variable referencing a [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm) object.```` ``` returnValue = configurationAppearanceColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationAppearanceColumn\_var" is a variable referencing a [ConfigurationAppearanceColumn](ConfigurationAppearanceColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationAppearanceCell](ConfigurationAppearanceCell.htm) | Returns the specified cell if successful and null if the name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowName | string | The name of the row to return the cell for. |

## Version

Introduced in version January 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |