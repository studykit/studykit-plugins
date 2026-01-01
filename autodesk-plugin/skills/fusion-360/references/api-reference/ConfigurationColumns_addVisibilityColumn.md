# ConfigurationColumns.addVisibilityColumn Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Adds a new column to control the visibility of an entity. If a visibility column already exists for the entity, the existing column is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addVisibilityColumn(entity) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.  ```` ``` #include <Fusion/Configurations/ConfigurationColumns.h>  returnValue = configurationColumns_var->addVisibilityColumn(entity); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationVisibilityColumn](ConfigurationVisibilityColumn.htm) | Returns the new column or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| entity | [Base](Base.htm) | Returns the entity whose visibility will be controlled by this column. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |