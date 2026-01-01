# ConfigurationMaterialColumns.add Method

Parent Object: [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationMaterialColumns.h>

## Description

Adds a new column to the material table. If you are adding the first column to the table and it is anything other than the root component, an additional column for the root component will automatically be created as the first column.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object.```` ``` returnValue = configurationMaterialColumns_var.add(entity) ``` ```` |

"configurationMaterialColumns\_var" is a variable referencing a [ConfigurationMaterialColumns](ConfigurationMaterialColumns.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationMaterialColumn](ConfigurationMaterialColumn.htm) | Returns the newly created ConfigurationMaterialColumn object or null if it fails. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | The component or body whose material will be controlled by this column. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |