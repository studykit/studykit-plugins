# ConfigurationColumns.addInsertColumn Method

Parent Object: [ConfigurationColumns](ConfigurationColumns.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Configurations/ConfigurationColumns.h>

## Description

Add a new column to control which configuration is used for an inserted configuration. If an insert column already exists for the occurrence, the existing column is returned.

## Syntax

* [Python](#Python)
* [C++](#C++)

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.```` ``` returnValue = configurationColumns_var.addInsertColumn(occurrence) ``` ```` |

"configurationColumns\_var" is a variable referencing a [ConfigurationColumns](ConfigurationColumns.htm) object.  ```` ``` #include <Fusion/Configurations/ConfigurationColumns.h>  returnValue = configurationColumns_var->addInsertColumn(occurrence); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [ConfigurationInsertColumn](ConfigurationInsertColumn.htm) | Returns the new column or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| occurrence | [Occurrence](Occurrence.htm) | The occurrence that references a configuration. |

## Version

Introduced in version March 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |