# ConfigurationFeatureAspectColumn.getCellByRowName Method

Parent Object: [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationFeatureAspectColumn.h>

## Description

Gets the cell in this column at the row specified by its name. Depending on the type of data in the cells within the column a ConfigurationFeatureAspectBooleanCell or ConfigurationFeatureAspectStringCell will be returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationFeatureAspectColumn\_var" is a variable referencing a [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm) object.```` ``` returnValue = configurationFeatureAspectColumn_var.getCellByRowName(rowName) ``` ```` |

"configurationFeatureAspectColumn\_var" is a variable referencing a [ConfigurationFeatureAspectColumn](ConfigurationFeatureAspectColumn.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationCell](ConfigurationCell.htm) | Returns the specified cell if successful and null if the name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| rowName | string | The name of the row to return the cell for. |

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |